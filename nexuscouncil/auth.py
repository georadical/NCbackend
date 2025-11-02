"""Authentication views with drf-spectacular schema integration.

Vistas de autenticación con integración de esquemas de drf-spectacular.
"""

from drf_spectacular.openapi import AutoSchema
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class SpectacularTokenObtainPairView(TokenObtainPairView):
    """Issue JWT tokens with an inspectable schema for drf-spectacular.

    Emite tokens JWT con un esquema detectable por drf-spectacular.
    """

    schema = AutoSchema()


class SpectacularTokenRefreshView(TokenRefreshView):
    """Refresh JWT tokens with an inspectable schema for drf-spectacular.

    Renueva tokens JWT con un esquema detectable por drf-spectacular.
    """

    schema = AutoSchema()

