"""Tests ensuring JWT views expose drf-spectacular schemas.

Pruebas que aseguran que las vistas JWT exponen esquemas de drf-spectacular.
"""

from drf_spectacular.openapi import AutoSchema

from nexuscouncil.auth import (
    SpectacularTokenObtainPairView,
    SpectacularTokenRefreshView,
)


def test_spectacular_token_views_use_auto_schema():
    """Check that token views provide AutoSchema instances to drf-spectacular.

    Verifica que las vistas de tokens ofrecen instancias de AutoSchema a drf-spectacular.
    """

    assert isinstance(SpectacularTokenObtainPairView.schema, AutoSchema)
    assert isinstance(SpectacularTokenRefreshView.schema, AutoSchema)

