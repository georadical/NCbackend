"""
PricingFeatureSerializer – NexusCouncil CMS

EN: Serializes individual pricing features linked to specific pricing plans in the “Simple, Transparent Pricing” section.
ES: Serializa las características individuales de los planes de precios mostradas en la sección “Precios simples y transparentes”.
"""

from rest_framework import serializers

from cms.models.pricing_feature import PricingFeature


class PricingFeatureSerializer(serializers.ModelSerializer):
    """Serializer for the PricingFeature model."""

    class Meta:
        model = PricingFeature
        fields = [
            "id",
            "plan",
            "description",
            "order",
            "included",
        ]
        read_only_fields = ["id"]
