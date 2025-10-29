"""
SiteSettingsViewSet – NexusCouncil CMS

EN: Read-only ViewSet exposing the global SiteSettings instance for branding, SEO, and social configuration.
ES: ViewSet de solo lectura que expone la instancia global de SiteSettings (marca, SEO y redes sociales).
"""

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from cms.models.sitesettings import SiteSettings
from cms.serializers.site_settings import SiteSettingsSerializer


class SiteSettingsViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only API for SiteSettings (only one instance expected)."""

    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=["get"], url_path="active")
    def get_active(self, request):
        """Return the first (active) SiteSettings instance."""
        instance = SiteSettings.objects.first()
        if not instance:
            return Response({"detail": "No site settings found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
