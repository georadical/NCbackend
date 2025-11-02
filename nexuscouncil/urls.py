"""Project URL routing including JWT token endpoints.

Enrutamiento de URL del proyecto que incluye los puntos finales de tokens JWT.
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from nexuscouncil.auth import (
    SpectacularTokenObtainPairView,
    SpectacularTokenRefreshView,
)

urlpatterns = [
    path("cms/", include("cms.urls")),
    path(
        "api/token/",
        SpectacularTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh/",
        SpectacularTokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

if "django.contrib.admin" in settings.INSTALLED_APPS:
    urlpatterns.insert(0, path("admin/", admin.site.urls))
