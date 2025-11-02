"""
HeroViewSet – NexusCouncil CMS

EN: Read-only ViewSet exposing the hero section (title, subtitle, CTAs, and background) for the landing page.
ES: ViewSet de solo lectura que expone la sección hero (título, subtítulo, CTAs y fondo) de la página de inicio.
"""

from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from cms.models.hero import Hero
from cms.serializers.hero import HeroSerializer


class HeroViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """API for managing and reading Hero sections."""
    """API para gestionar y leer las secciones Hero."""

    serializer_class = HeroSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """Return queryset scoped by action to expose active heroes by default."""
        """Devuelve el queryset según la acción para exponer héroes activos por defecto."""
        if getattr(self, "action", None) in {"list", "get_active"}:
            return Hero.objects.filter(is_active=True).order_by("-created_at")
        return Hero.objects.all().order_by("-created_at")

    @action(detail=False, methods=["get"], url_path="active")
    def get_active(self, request):
        """Return the currently active Hero section."""
        instance = Hero.objects.filter(is_active=True).first()
        if not instance:
            return Response({"detail": "No active hero found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
