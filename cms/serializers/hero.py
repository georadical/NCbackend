"""
HeroSerializer – NexusCouncil CMS

EN: Serializes the hero section of the landing page, exposing title, subtitle, call-to-actions, and background configuration.
ES: Serializa la sección hero de la página de inicio, exponiendo título, subtítulo, llamados a la acción y configuración del fondo.
"""

from django.db import transaction
from rest_framework import serializers

from cms.models.hero import Hero


class HeroSerializer(serializers.ModelSerializer):
    """Serializer for the Hero model with create support."""
    """Serializador para el modelo Hero con soporte de creación."""

    bg_media = serializers.ImageField(write_only=True, required=False, allow_null=True)
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
            "bg_media",
            "bg_media_url",
            "is_active",
        ]
        read_only_fields = ["id", "bg_media_url"]

    def get_bg_media_url(self, obj):
        """Return absolute URL for hero background image if present."""
        """Devuelve la URL absoluta de la imagen de fondo si existe."""
        if not obj.bg_media:
            return None
        request = self.context.get("request")
        return request.build_absolute_uri(obj.bg_media.url) if request else obj.bg_media.url

    def validate(self, attrs):
        """Ensure background media presence matches the background type."""
        """Garantiza que la presencia de fondo coincida con el tipo configurado."""
        bg_type = attrs.get("bg_type", getattr(self.instance, "bg_type", None))
        bg_media = attrs.get("bg_media", getattr(self.instance, "bg_media", None))
        if bg_type == "image" and not bg_media:
            raise serializers.ValidationError(
                {"bg_media": "Background image is required when bg_type is 'image'."}
            )
        return attrs

    def create(self, validated_data):
        """Create hero ensuring only one active instance exists."""
        """Crea un hero garantizando que solo exista una instancia activa."""
        default_active = Hero._meta.get_field("is_active").default
        is_active = validated_data.get("is_active", default_active)
        with transaction.atomic():
            if is_active:
                Hero.objects.filter(is_active=True).update(is_active=False)
            return super().create(validated_data)
