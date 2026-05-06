from django.http import JsonResponse
from django.views import View


class PingServer(View):
    def get(self, request):
        return JsonResponse({
            'res': 'pong'
        })
