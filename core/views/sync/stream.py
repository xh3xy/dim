from core.decorators.is_authenticated import is_authenticated
from core.enums.sync_entity_type import SyncEntityType
from core.enums.sync_request_type import SyncRequestType
from core.models.user import User
from core.models.session import Session
from core.models.sync_checkpoint import SyncCheckpoint
from core.utils.timezone_serializer import timezone_serializer
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from typing import cast
import json
import time
import uuid

MAX_DAYS = 30
MAX_DURATION = MAX_DAYS * 24 * 60 * 60 * 1000


@method_decorator(is_authenticated, name='dispatch')
class SyncStream(View):
    def post(self, request):
        def needs_full_sync(checkpoints):
            complete_ack = checkpoints.filter(type=SyncEntityType.SYNCCOMPLETEV1).first()
            if not complete_ack:
                return False

            return complete_ack.update_id.int >> 80 < int(time.time() * 1000) - MAX_DURATION

        def user_jsonl(sync_type, user):
            return json.dumps({
                'type': sync_type,
                'data': {
                    'id': str(user.id),
                    'name': user.name,
                    'email': user.email,
                    'avatarColor': user.avatar_color,
                    'deletedAt': timezone_serializer(user.deleted_at) if user.deleted_at else None,
                    'profileChangedAt': timezone_serializer(user.profile_changed_at),
                    'isAdmin': user.is_admin,
                    'pinCode': user.pin_code,
                    'oauthId': user.oauth_id,
                    'storageLabel': user.storage_label,
                    'quotaSizeInBytes': user.quota_size_in_bytes,
                    'quotaUsageInBytes': user.quota_usage_in_bytes,
                    'hasProfileImage': user.profile_image != None,
                },
                'ack': f'{sync_type}|{str(user.update_id)}',
            })

        session = cast(Session, request.user)
        user = session.user_id
        body = json.loads(request.body)

        response_body = []

        reset = body.get('reset', False) == True

        if reset:
            Session.objects.filter(id=session.id).update(is_pending_sync_reset=False)
            SyncCheckpoint.objects.filter(session=session).delete()

        if session.is_pending_sync_reset:
            return JsonResponse(
                {
                    'type': SyncEntityType.SYNCRESETV1.value,
                    'data': {},
                    'ack': f'{SyncEntityType.SYNCRESETV1.value}|reset',
                },
                content_type='application/jsonlines+json',
            )

        current_checkpoints = SyncCheckpoint.objects.filter(session=session)
        checkpoints_map = {c.type: c for c in current_checkpoints}
        if needs_full_sync(current_checkpoints):
            return JsonResponse(
                {
                    'type': SyncEntityType.SYNCRESETV1.value,
                    'data': {},
                    'ack': f'{SyncEntityType.SYNCRESETV1.value}|reset',
                },
                content_type='application/jsonlines+json',
            )

        requested_checkpoints = set()
        for ack in body['types']:
            requested_checkpoints.add(ack)

        now_id = uuid.uuid7()

        # TODO: Add missing RequestTypes

        # AuthUsersV1
        if SyncRequestType.AUTHUSERSV1.value in requested_checkpoints:
            sync_type = SyncEntityType.AUTHUSERV1
            ack = checkpoints_map.get(sync_type)

            qs = User.objects.filter(
                id=user.id,
                update_id__lt=now_id,
            )
            if ack:
                qs = qs.filter(update_id__gt=ack.update_id)

            if qs:
                response_body.append(user_jsonl(sync_type.value, qs.first()))


        # UsersV1
        if SyncRequestType.USERSV1.value in requested_checkpoints:
            sync_type = SyncEntityType.USERV1.value
            ack = checkpoints_map.get(sync_type)

            qs = User.objects.filter(update_id__lt=now_id)
            if ack:
                qs = qs.filter(update_id__gt=ack.update_id)

            if qs:
                for user in qs:
                    response_body.append(user_jsonl(sync_type, user))


        # SyncComplete
        sync_type = SyncEntityType.SYNCCOMPLETEV1.value
        response_body.append(
            json.dumps({
                'type': sync_type,
                'data': {},
                'ack': f'{sync_type}|{str(now_id)}',
            })
        )

        return HttpResponse(
            '\n'.join(response_body) + '\n',
            content_type='application/jsonlines+json',
        )
