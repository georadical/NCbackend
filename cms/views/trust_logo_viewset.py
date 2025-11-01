"""
TrustLogoViewSet – NexusCouncil CMS

EN: Read-only ViewSet exposing active partner/council logos for the “Trusted by” section.
ES: ViewSet de solo lectura que expone los logotipos activos de socios o consejos en la sección “Confiado por”.
"""

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from cms.models.trust_logo import TrustLogo
from cms.serializers.trust_logo import TrustLogoSerializer


class TrustLogoViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only API for TrustLogo model."""

    queryset = TrustLogo.objects.filter(is_active=True).order_by("order")
    serializer_class = TrustLogoSerializer
    permission_classes = [AllowAny]
