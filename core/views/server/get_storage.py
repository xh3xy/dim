from core.decorators.is_authenticated import is_authenticated
from core.utils.bytes import as_human_readable
from django.conf import settings
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
import shutil


@method_decorator(is_authenticated, name='dispatch')
class GetStorage(View):
    def get(self, request):
        total, used, free = shutil.disk_usage(settings.MEDIA_ROOT)

        disk_percentage = round((total - free) / total, 2)

        return JsonResponse({
            'diskAvailable': as_human_readable(free),
            'diskAvailableRaw': free,
            'diskSize': total,
            'diskSizeRaw': as_human_readable(total),
            'diskUsagePercentage': disk_percentage,
            'diskUse': as_human_readable(used),
            'diskUseRaw': used,
        })
