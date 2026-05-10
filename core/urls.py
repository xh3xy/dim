from core.views.authentication.login import Login
from core.views.authentication.validate_access_token import ValidateAccessToken
from core.views.server.get_server_config import GetServerConfig
from core.views.server.get_server_features import GetServerFeatures
from core.views.server.get_server_version import GetServerVersion
from core.views.server.get_storage import GetStorage
from core.views.server.ping_server import PingServer
from core.views.users.get_my_user import GetMyUser
from core.views.well_known.immich import WellknownImmich
from django.urls import path


urlpatterns = [
    path('.well-known/immich', WellknownImmich.as_view()),

    path('api/auth/login', Login.as_view()),
    path('api/auth/validateToken', ValidateAccessToken.as_view()),

    path('api/server/config', GetServerConfig.as_view()),
    path('api/server/features', GetServerFeatures.as_view()),
    path('api/server/ping', PingServer.as_view()),
    path('api/server/storage', GetStorage.as_view()),
    path('api/server/version', GetServerVersion.as_view()),

    path('api/users/me', GetMyUser.as_view()),
]
