"""
GlimpseImageSerializer – NexusCouncil CMS

EN: Serializes the platform preview images for the “A Glimpse of the Platform” section, including optional captions and order.
ES: Serializa las imágenes de vista previa de la plataforma para la sección “Una mirada a la plataforma”, incluyendo subtítulos opcionales y su orden.
"""

from rest_framework import serializers

from cms.models.glimpse_image import GlimpseImage


class GlimpseImageSerializer(serializers.ModelSerializer):
    """Serializer for the GlimpseImage model."""

    image_url = serializers.SerializerMethodField()

    class Meta:
        model = GlimpseImage
        fields = [
            "id",
            "image_url",
            "title",
            "caption",
            "order",
            "is_active",
        ]
        read_only_fields = ["id"]

    def get_image_url(self, obj):
        """Return absolute URL for image if present."""
        request = self.context.get("request")
        if request and obj.image:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url if obj.image else None
