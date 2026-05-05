from django.http import JsonResponse
from django.views import View


class ServerConfig(View):
    def get(self, request):
        #TODO: Hardcoded
        return JsonResponse({
            'externalDomain': '',
            'isInitialized': True,
            'isOnboarded': True,
            'loginPageMessage': '',
            'maintenanceMode': False,
            'mapDarkStyleUrl':  "https://tiles.immich.cloud/v1/style/dark.json",
            'mapLightStyleUrl':  "https://tiles.immich.cloud/v1/style/light.json",
            'oauthButtonText': 'Login with OAuth',
            'publicUsers': True,
            'trashDays': 30,
            'userDeleteDelay': 7,
        })