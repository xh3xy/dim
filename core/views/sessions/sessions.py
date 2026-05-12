from core.decorators.is_authenticated import is_authenticated
from core.models.session import Session
from core.utils.timezone_serializer import timezone_serializer
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from typing import cast


@method_decorator(is_authenticated, name='dispatch')
class Sessions(View):
    def get(self, request):
        session = cast(Session, request.user)

        sessions = Session.objects.filter(user_id=session.user_id)

        return JsonResponse([
            {
                'id': str(session.id),
                'createdAt': timezone_serializer(session.created_at),
                'updatedAt': timezone_serializer(session.updated_at),
                'current': session == request.user,
                'appVersion': session.app_version,
                'deviceOS': session.device_os,
                'deviceType': session.device_type,
                'isPendingSyncReset': session.is_pending_sync_reset,
            } for session in sessions
        ], safe=False)

    def delete(self, request):
        session = cast(Session, request.user)

        Session.objects.filter(user_id=session.user_id).delete()

        return HttpResponse(status=204)
