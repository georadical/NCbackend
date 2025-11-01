"""
HeroViewSet – NexusCouncil CMS

EN: Read-only ViewSet exposing the hero section (title, subtitle, CTAs, and background) for the landing page.
ES: ViewSet de solo lectura que expone la sección hero (título, subtítulo, CTAs y fondo) de la página de inicio.
"""

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from cms.models.hero import Hero
from cms.serializers.hero import HeroSerializer


class HeroViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only API for the Hero section."""

    queryset = Hero.objects.filter(is_active=True).order_by("-created_at")
    serializer_class = HeroSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=["get"], url_path="active")
    def get_active(self, request):
        """Return the currently active Hero section."""
        instance = Hero.objects.filter(is_active=True).first()
        if not instance:
            return Response({"detail": "No active hero found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
