from core.constants import LOGIN_URL
from core.decorators.is_authenticated import is_authenticated
from core.enums.immich_cookie import ImmichCookie
from core.models.session import Session
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(is_authenticated, name='dispatch')
class Logout(View):
    def post(self, request):
        Session.objects.get(id=request.user).delete()

        # TODO: Missing OAuth uri?

        response = JsonResponse({
            'successful': True,
            'redirectUri': LOGIN_URL,
        })

        response.delete_cookie(ImmichCookie.ACCESS_TOKEN)
        response.delete_cookie(ImmichCookie.AUTH_TYPE)
        response.delete_cookie(ImmichCookie.IS_AUTHENTICATED)

        return response
