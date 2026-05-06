from django.http import JsonResponse
from django.views import View


class GetServerFeatures(View):
    def get(self, request):
        #TODO: Hardcoded
        return JsonResponse({
            'configFile': False,
            'duplicateDetection': False,
            'email': False,
            'facialRecognition': True,
            'importFaces': True,
            'map': True,
            'oauth': False,
            'oauthAutoLaunch': False,
            'ocr': True,
            'passwordLogin': True,
            'reverseGeocoding': True,
            'search': True,
            'sidecar': True,
            'smartSearch': True,
            'trash': True,
        })