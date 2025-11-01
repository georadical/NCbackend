"""
FooterLinkViewSet – NexusCouncil CMS

EN: Read-only ViewSet exposing individual footer links for display in the website footer.
ES: ViewSet de solo lectura que expone los enlaces individuales del pie de página.
"""

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from cms.models.footer_link import FooterLink
from cms.serializers.footer_link import FooterLinkSerializer


class FooterLinkViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only API for FooterLink model."""

    queryset = FooterLink.objects.filter(is_active=True).order_by("group__order", "order")
    serializer_class = FooterLinkSerializer
    permission_classes = [AllowAny]
