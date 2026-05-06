from django.db import models


class ImmichCookie(models.TextChoices):
    ACCESS_TOKEN = 'immich_access_token', 'AccessToken'
    MAINTENANCE_TOKEN = 'immich_maintenance_token', 'MaintenanceToken'
    AUTH_TYPE = 'immich_auth_type', 'AuthType'
    IS_AUTHENTICATED = 'immich_is_authenticated', 'IsAuthenticated'
    SHARED_LINK_TOKEN = 'immich_shared_link_token', 'SharedLinkToken'
    OAUTHSTATE = 'immich_oauth_state', 'OAuthState'
    OAUTHCODEVERIFIER = 'immich_oauth_code_verifier', 'OAuthCodeVerifier'
