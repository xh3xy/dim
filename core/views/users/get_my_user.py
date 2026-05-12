from core.decorators.is_authenticated import is_authenticated
from core.models.user import User
from core.utils.timezone_serializer import timezone_serializer
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from typing import cast


@method_decorator(is_authenticated, name='dispatch')
class GetMyUser(View):
    def get(self, request):
        user = cast(User, request.user.user_id)

        return JsonResponse({
            'id': user.id,
            'email': user.email,
            'name': user.name,
            'profileImagePath': user.profile_image if user.profile_image else '',
            'avatarColor': user.avatar_color,
            'profileChangedAt': timezone_serializer(user.profile_changed_at),
            'storageLabel': user.storage_label,
            'shouldChangePassword': user.should_change_password,
            'isAdmin': user.is_admin,
            'createdAt': timezone_serializer(user.created_at),
            'deletedAt': timezone_serializer(user.deleted_at) if user.deleted_at else user.deleted_at,
            'updatedAt': timezone_serializer(user.updated_at),
            'oauthId': user.oauth_id,
            'quotaSizeInBytes': user.quota_size_in_bytes,
            'quotaUsageInBytes': user.quota_usage_in_bytes,
            'status': user.status,
            'license': None, #TODO: Hardcoded
        })
