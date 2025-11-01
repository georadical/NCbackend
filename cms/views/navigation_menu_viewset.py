"""
NavigationMenuViewSet – NexusCouncil CMS

EN: Read-only ViewSet exposing header and footer navigation menus with their ordered items.
ES: ViewSet de solo lectura que expone los menús de navegación de encabezado y pie con sus elementos ordenados.
"""

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from cms.models.navigation_menu import NavigationMenu
from cms.serializers.navigation_menu import NavigationMenuSerializer


class NavigationMenuViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only ViewSet for NavigationMenu with header/footer filtering."""

    queryset = NavigationMenu.objects.prefetch_related("items").all()
    serializer_class = NavigationMenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=["get"], url_path="header")
    def get_header(self, request):
        """Return header navigation menu."""
        header = NavigationMenu.objects.filter(placement="header").first()
        if not header:
            return Response({"detail": "Header menu not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(self.get_serializer(header).data)

    @action(detail=False, methods=["get"], url_path="footer")
    def get_footer(self, request):
        """Return footer navigation menu."""
        footer = NavigationMenu.objects.filter(placement="footer").first()
        if not footer:
            return Response({"detail": "Footer menu not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(self.get_serializer(footer).data)
