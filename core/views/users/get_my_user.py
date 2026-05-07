from core.decorators.is_authenticated import is_authenticated
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views import View
from typing import cast
from core.models.user import User
from core.utils.timezone_serializer import timezone_serializer


@method_decorator(is_authenticated, name='dispatch')
class GetMyUser(View):
    def get(self, request):
        user = request.user

        return JsonResponse({
            'id': user.id,
            'email': user.email,
            'name': user.name,
            'profileImagePath': user.profile_image if user.profile_image else '',
            'avatarColor': 'blue', #TODO: Hardcoded
            'profileChangedAt': timezone_serializer(user.profile_changed_at),
            'storageLabel': 'admin', #TODO: Hardcoded
            'shouldChangePassword': user.should_change_password,
            'isAdmin': user.is_admin,
            'createdAt': timezone_serializer(user.created_at),
            'deletedAt': None, #TODO: Hardcoded
            'updatedAt': timezone_serializer(user.updated_at),
            'oauthId': '', #TODO: Hardcoded
            'quotaSizeInBytes': None, #TODO: Hardcoded
            'quotaUsageInBytes': 193684647845, #TODO: Hardcoded
            'status': user.status,
            'license': None, #TODO: Hardcoded
        })
