"""
PricingFeatureViewSet – NexusCouncil CMS

EN: Read-only ViewSet exposing individual features associated with pricing plans in the “Simple, Transparent Pricing” section.
ES: ViewSet de solo lectura que expone las características asociadas a los planes de precios en la sección “Precios simples y transparentes”.
"""

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from cms.models.pricing_feature import PricingFeature
from cms.serializers.pricing_feature import PricingFeatureSerializer


class PricingFeatureViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only API for PricingFeature model."""

    queryset = PricingFeature.objects.select_related("plan").order_by("plan__order", "order")
    serializer_class = PricingFeatureSerializer
    permission_classes = [AllowAny]
