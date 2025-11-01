"""
IntegrationSerializer – NexusCouncil CMS

EN: Serializes integration partners and their logos for the “Seamlessly Integrated” section.
ES: Serializa las plataformas asociadas e integraciones con sus logotipos para la sección “Integración sin esfuerzo”.
"""

from rest_framework import serializers

from cms.models.integration import Integration


class IntegrationSerializer(serializers.ModelSerializer):
    """Serializer for the Integration model."""

    logo_url = serializers.SerializerMethodField()

    class Meta:
        model = Integration
        fields = [
            "id",
            "name",
            "logo_url",
            "website_url",
            "order",
            "is_active",
        ]
        read_only_fields = ["id"]

    def get_logo_url(self, obj):
        """Return absolute URL for the logo if present."""
        request = self.context.get("request")
        if request and obj.logo:
            return request.build_absolute_uri(obj.logo.url)
        return obj.logo.url if obj.logo else None
