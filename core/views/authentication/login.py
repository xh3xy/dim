from core.models.user import User
from django.http import JsonResponse
from django.views import View
import json


class Login(View):
    def post(self, request):
        data = json.loads(request.body)

        email = data.get('email')
        password = data.get('password')

        user = User.objects.get(email=email)
        if user.check_password(password):
            #TODO: Hardcoded
            return JsonResponse({
                "accessToken": "xxx", #TODO: Hardcoded
                "userId": user.id,
                "userEmail": user.email,
                "name": user.name,
                "isAdmin": user.is_admin,
                "profileImagePath": user.profile_image.url if user.profile_image else '',
                "shouldChangePassword": user.should_change_password,
                "isOnboarded": True, #TODO: Hardcoded
            })
