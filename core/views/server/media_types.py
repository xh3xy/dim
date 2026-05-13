from core.utils.mime_types import image
from core.utils.mime_types import sidecar
from core.utils.mime_types import video
from django.http import JsonResponse
from django.views import View


class MediaTypes(View):
    def get(self, request):
        return JsonResponse({
            'image': [key for key in image.keys()],
            'video': [key for key in video.keys()],
            'sidecar': [key for key in sidecar.keys()],
        })
