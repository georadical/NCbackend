"""
IntegrationViewSet – NexusCouncil CMS

EN: Read-only ViewSet exposing integration partners and their logos for the “Seamlessly Integrated” section.
ES: ViewSet de solo lectura que expone las plataformas asociadas y sus logotipos en la sección “Integración sin esfuerzo”.
"""

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from cms.models.integration import Integration
from cms.serializers.integration import IntegrationSerializer


class IntegrationViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only API for Integration model."""

    queryset = Integration.objects.filter(is_active=True).order_by("order", "name")
    serializer_class = IntegrationSerializer
    permission_classes = [AllowAny]
