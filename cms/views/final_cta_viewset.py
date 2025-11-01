"""
FinalCTAViewSet – NexusCouncil CMS

EN: Read-only ViewSet exposing the final call-to-action content for the “Ready to Build a Smarter Council?” section.
ES: ViewSet de solo lectura que expone el contenido del llamado final a la acción en la sección “¿Listo para construir un consejo más inteligente?”.
"""

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from cms.models.final_cta import FinalCTA
from cms.serializers.final_cta import FinalCTASerializer


class FinalCTAViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only API for FinalCTA model."""

    queryset = FinalCTA.objects.filter(is_active=True).order_by("order")
    serializer_class = FinalCTASerializer
    permission_classes = [AllowAny]
