"""
SiteSettingsSerializer – NexusCouncil CMS

EN: Serializes the global site configuration for the frontend (branding, colors, SEO, and social links).
ES: Serializa la configuración global del sitio para el frontend (marca, colores, SEO y redes sociales).
"""

from rest_framework import serializers

from cms.models.sitesettings import SiteSettings


class SiteSettingsSerializer(serializers.ModelSerializer):
    """Serializer for the SiteSettings model."""

    logo_url = serializers.SerializerMethodField()
    og_image_url = serializers.SerializerMethodField()

    class Meta:
        model = SiteSettings
        fields = [
            "id",
            "site_name",
            "theme_primary",
            "theme_bg_light",
            "theme_bg_dark",
            "twitter_url",
            "linkedin_url",
            "youtube_url",
            "meta_title",
            "meta_description",
            "logo_url",
            "og_image_url",
        ]
        read_only_fields = ["id"]

    def get_logo_url(self, obj):
        """Return absolute URL for logo if present."""
        request = self.context.get("request")
        return request.build_absolute_uri(obj.logo.url) if obj.logo else None

    def get_og_image_url(self, obj):
        """Return absolute URL for Open Graph image if present."""
        request = self.context.get("request")
        return request.build_absolute_uri(obj.og_image.url) if obj.og_image else None
