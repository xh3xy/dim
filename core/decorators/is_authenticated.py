from core.enums.immich_cookie import ImmichCookie
from core.models.session import Session
from django.http import JsonResponse
from functools import wraps
import hashlib

def is_authenticated(view):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        token = request.COOKIES.get(ImmichCookie.ACCESS_TOKEN)
        if not token:
            return JsonResponse({
                "message": "Authentication required",
                "error": "Unauthorized",
                "statusCode": 401,
                "correlationId": "12mvwv78", #TODO: Hardcoded
            }, status=401)

        hashed = hashlib.sha256(token.encode()).hexdigest()

        try:
            session = Session.objects.select_related('user_id').get(token=hashed.encode())
            request.user = session.user_id
        except Session.DoesNotExist:
            return JsonResponse({
                "message": "Invalid user token",
                "error": "Unauthorized",
                "statusCode": 401,
                "correlationId": "ylc6yoqs", #TODO: Hardcoded
            }, status=401)

        return view(request, *args, **kwargs)
    return wrapper
