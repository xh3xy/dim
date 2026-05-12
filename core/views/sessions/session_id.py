from core.decorators.is_authenticated import is_authenticated
from core.models.session import Session
from core.utils.timezone_serializer import timezone_serializer
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from typing import cast


@method_decorator(is_authenticated, name='dispatch')
class SessionId(View):
    def delete(self, request, session_id):
        session = cast(Session, request.user)

        Session.objects.filter(id=session_id).delete()

        return HttpResponse(status=204)
