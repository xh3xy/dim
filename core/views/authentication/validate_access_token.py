from core.decorators.is_authenticated import is_authenticated
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(is_authenticated, name='dispatch')
class ValidateAccessToken(View):
    def post(self, request):
        return JsonResponse({
            "authStatus": True,
        })
