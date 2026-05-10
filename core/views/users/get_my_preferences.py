from core.decorators.is_authenticated import is_authenticated
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(is_authenticated, name='dispatch')
class GetMyPreferences(View):
    def get(self, request):
        # TODO: Hardcoded
        return JsonResponse({
            'albums': {
                'defaultAssetOrder': 'desc'
            },
            'folders': {
                'enabled': False,
                'sidebarWeb': False
            },
            'memories': {
                'enabled': True,
                'duration': 5
            },
            'people': {
                'enabled': True,
                'sidebarWeb': False
            },
            'sharedLinks': {
                'enabled': True,
                'sidebarWeb': False
            },
            'ratings': {
                'enabled': False
            },
            'tags': {
                'enabled': False,
                'sidebarWeb': False
            },
            'emailNotifications': {
                'enabled': True,
                'albumInvite': True,
                'albumUpdate': True
            },
            'download': {
                'archiveSize': 4294967296,
                'includeEmbeddedVideos': False
            },
            'purchase': {
                'showSupportBadge': True,
                'hideBuyButtonUntil': '2124-10-17T08:13:35.665Z'
            },
            'cast': {
                'gCastEnabled': False
            }
        })
