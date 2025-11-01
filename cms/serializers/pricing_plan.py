"""
PricingPlanSerializer – NexusCouncil CMS

EN: Serializes pricing plan tiers, including name, description, features, price, and whether it's the highlighted (“Most Popular”) plan.
ES: Serializa los niveles de planes de precios, incluyendo nombre, descripción, características, precio y si es el plan destacado (“Más popular”).
"""

from rest_framework import serializers

from cms.models.pricing_plan import PricingPlan


class PricingPlanSerializer(serializers.ModelSerializer):
    """Serializer for the PricingPlan model."""

    class Meta:
        model = PricingPlan
        fields = [
            "id",
            "name",
            "description",
            "price",
            "highlight",
            "order",
            "features",
            "is_active",
        ]
        read_only_fields = ["id"]
