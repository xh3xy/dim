from core.enums.auth_type import AuthType
from core.enums.immich_cookie import ImmichCookie
from core.models.session import Session
from core.models.user import User
from core.utils.request import get_user_agent_details
from django.http import JsonResponse
from django.views import View
import hashlib
import json
import secrets


class Login(View):
    def post(self, request):
        data = json.loads(request.body)

        email = data.get('email')
        password = data.get('password')

        user = User.objects.get(email=email)
        if user.check_password(password):
            #TODO: Should this be moved away?
            token = secrets.token_urlsafe(32)
            hashed = hashlib.sha256(token.encode()).hexdigest()

            login_details = get_user_agent_details(request.headers)

            Session.objects.create(
                token=hashed.encode(),
                device_os=login_details['device_os'],
                device_type=login_details['device_type'],
                app_version=login_details['app_version'],
                user_id=user,
            )

            #TODO: Hardcoded
            response = JsonResponse({
                "accessToken": token,
                "userId": user.id,
                "userEmail": user.email,
                "name": user.name,
                "isAdmin": user.is_admin,
                "profileImagePath": user.profile_image.url if user.profile_image else '',
                "shouldChangePassword": user.should_change_password,
                "isOnboarded": True, #TODO: Hardcoded
            })

            response.set_cookie(
                ImmichCookie.ACCESS_TOKEN,
                token,
                max_age=34560000,
                httponly=True,
                samesite='Lax'
            )

            response.set_cookie(
                ImmichCookie.AUTH_TYPE,
                AuthType.PASSWORD,
                max_age=34560000,
                httponly=True,
                samesite='Lax'
            )

            response.set_cookie(
                ImmichCookie.IS_AUTHENTICATED,
                'true',
                max_age=34560000,
                samesite='Lax'
            )

            return response
