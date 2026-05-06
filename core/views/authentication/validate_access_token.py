from core.enums.immich_cookie import ImmichCookie
from core.models.session import Session
from django.http import JsonResponse
from django.views import View
import hashlib


class ValidateAccessToken(View):
    def post(self, request):
        token = request.COOKIES.get(ImmichCookie.ACCESS_TOKEN)
        hashed = hashlib.sha256(token.encode()).hexdigest()

        exists = Session.objects.filter(token=hashed.encode()).exists()

        return JsonResponse({
            "authStatus": exists,
        })
