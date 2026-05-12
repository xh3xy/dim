from core.decorators.is_authenticated import is_authenticated
from core.enums.sync_entity_type import SyncEntityType
from core.models.session import Session
from core.models.sync_checkpoint import SyncCheckpoint
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from typing import cast
import json


@method_decorator(is_authenticated, name='dispatch')
class SyncAck(View):
    def get(self, request):
        session = cast(Session, request.user)

        checkpoints = SyncCheckpoint.objects.filter(session=session)
        return JsonResponse([
            {
                'type': checkpoint.type,
                'ack': checkpoint.ack,
            } for checkpoint in checkpoints
        ], safe=False)

    def post(self, request):
        session = cast(Session, request.user)
        body = json.loads(request.body)

        checkpoints = {}

        for ack in body['acks']:
            name, update_id, *extra = ack.split('|')

            if name not in SyncEntityType.values:
                continue

            if name == SyncEntityType.SYNCRESETV1:
                Session.objects.filter(id=session.id).update(is_pending_sync_reset=False)
                SyncCheckpoint.objects.filter(session=session).delete()
                return HttpResponse(status=204)

            checkpoints[name] = {
                'session': session,
                'type': name,
                'ack': ack,
                'update_id': update_id
            }

        for checkpoint in checkpoints.values():
            SyncCheckpoint.objects.update_or_create(
                session=session,
                type=checkpoint['type'],
                defaults={
                    'ack': checkpoint['ack'],
                    'update_id': checkpoint['update_id'],
                },
            )

        return HttpResponse(status=204)

    def delete(self, request):
        session = cast(Session, request.user)
        body = json.loads(request.body)

        checkpoints = []

        for ack in body['acks']:
            name, *extra = ack.split('|')

            if name not in SyncEntityType.values:
                continue

            checkpoints.append(name)

        SyncCheckpoint.objects.filter(
            session=session,
            type__in=checkpoints,
        ).delete()

        return HttpResponse(status=204)
