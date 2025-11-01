"""
HeroSerializer – NexusCouncil CMS

EN: Serializes the hero section of the landing page, exposing title, subtitle, call-to-actions, and background configuration.
ES: Serializa la sección hero de la página de inicio, exponiendo título, subtítulo, llamados a la acción y configuración del fondo.
"""

from rest_framework import serializers

from cms.models.hero import Hero


class HeroSerializer(serializers.ModelSerializer):
    """Serializer for the Hero model."""

    bg_media_url = serializers.SerializerMethodField()

    class Meta:
        model = Hero
        fields = [
            "id",
            "title",
            "subtitle",
            "cta_primary_label",
            "cta_primary_href",
            "cta_secondary_label",
            "cta_secondary_href",
            "bg_type",
            "bg_media_url",
            "is_active",
        ]
        read_only_fields = ["id"]

    def get_bg_media_url(self, obj):
        """Return absolute URL for hero background image if present."""
        if not obj.bg_media:
            return None
        request = self.context.get("request")
        return request.build_absolute_uri(obj.bg_media.url) if request else obj.bg_media.url
