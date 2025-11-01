"""
TrustLogoSerializer – NexusCouncil CMS

EN: Serializes partner or organization logos for display in the “Trusted by forward-thinking local governments” section.
ES: Serializa los logotipos de socios u organizaciones para mostrarlos en la sección “Confiado por gobiernos locales visionarios”.
"""

from rest_framework import serializers

from cms.models.trust_logo import TrustLogo


class TrustLogoSerializer(serializers.ModelSerializer):
    """Serializer for the TrustLogo model."""

    image_url = serializers.SerializerMethodField()

    class Meta:
        model = TrustLogo
        fields = ["id", "name", "image_url", "link", "order", "is_active"]
        read_only_fields = ["id"]

    def get_image_url(self, obj):
        """Return absolute URL for logo image if present."""
        if not obj.image:
            return None
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url) if request else obj.image.url
