"""
GlimpseImageViewSet – NexusCouncil CMS

EN: Read-only ViewSet exposing platform preview images for the “A Glimpse of the Platform” section.
ES: ViewSet de solo lectura que expone las imágenes de vista previa de la plataforma para la sección “Una mirada a la plataforma”.
"""

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from cms.models.glimpse_image import GlimpseImage
from cms.serializers.glimpse_image import GlimpseImageSerializer


class GlimpseImageViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only API for GlimpseImage model."""

    queryset = GlimpseImage.objects.filter(is_active=True).order_by("order")
    serializer_class = GlimpseImageSerializer
    permission_classes = [AllowAny]
