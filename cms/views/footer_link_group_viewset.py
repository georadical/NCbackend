"""
FooterLinkGroupViewSet – NexusCouncil CMS

EN: Read-only ViewSet exposing footer link groups (e.g., Product, Company, Legal) for the website footer.
ES: ViewSet de solo lectura que expone los grupos de enlaces del pie de página (por ejemplo, Producto, Empresa, Legal) para el sitio web.
"""

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from cms.models.footer_link_group import FooterLinkGroup
from cms.serializers.footer_link_group import FooterLinkGroupSerializer


class FooterLinkGroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only API for FooterLinkGroup model."""

    queryset = FooterLinkGroup.objects.filter(is_active=True).order_by("order")
    serializer_class = FooterLinkGroupSerializer
    permission_classes = [AllowAny]
