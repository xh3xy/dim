from core.decorators.is_authenticated import is_authenticated
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from core.models.api_key import ApiKey
from typing import cast
from core.models.session import Session
from core.utils.timezone_serializer import timezone_serializer


@method_decorator(is_authenticated, name='dispatch')
class ApiKeys(View):
    def get(self, request):
        session = cast(Session, request.user)

        keys = ApiKey.objects.filter(user=session.user_id).order_by('-created_at')

        return JsonResponse([
            {
                "id": key.id,
                "name": key.name,
                "createdAt": timezone_serializer(key.created_at),
                "updatedAt": timezone_serializer(key.updated_at),
                # TODO: Hardcoded
                "permissions": [
                    "all"
                ]
            } for key in keys
        ], safe=False)
