"""
PricingPlanViewSet – NexusCouncil CMS

EN: Read-only ViewSet exposing pricing plans for the “Simple, Transparent Pricing” section.
ES: ViewSet de solo lectura que expone los planes de precios para la sección “Precios simples y transparentes”.
"""

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from cms.models.pricing_plan import PricingPlan
from cms.serializers.pricing_plan import PricingPlanSerializer


class PricingPlanViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only API for PricingPlan model."""

    queryset = PricingPlan.objects.filter(is_active=True).order_by("order")
    serializer_class = PricingPlanSerializer
    permission_classes = [AllowAny]
