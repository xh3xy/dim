from core.views.auth.login import AuthLogin
from core.views.server.config import ServerConfig
from core.views.server.features import ServerFeatures
from core.views.server.ping import ServerPing
from core.views.server.version import ServerVersion
from core.views.well_known.immich import WellknownImmich
from django.urls import path


urlpatterns = [
    path('.well-known/immich', WellknownImmich.as_view()),

    path('api/auth/login', AuthLogin.as_view()),

    path('api/server/config', ServerConfig.as_view()),
    path('api/server/features', ServerFeatures.as_view()),
    path('api/server/ping', ServerPing.as_view()),
    path('api/server/version', ServerVersion.as_view())
]
