from django.http import JsonResponse
from django.views import View


class ServerPing(View):
    def get(self, request):
        return JsonResponse({
            'res': 'pong'
        })
