"""
UseCaseFeatureSerializer – NexusCouncil CMS

EN: Serializes use case features that describe specific real-world challenges and their solutions, including related tags.
ES: Serializa las funcionalidades o casos de uso que describen desafíos reales y sus soluciones, incluyendo las etiquetas relacionadas.
"""

from rest_framework import serializers

from cms.models.use_case_feature import UseCaseFeature
from cms.serializers.use_case_tag import UseCaseTagSerializer


class UseCaseFeatureSerializer(serializers.ModelSerializer):
    """Serializer for the UseCaseFeature model."""

    image_url = serializers.SerializerMethodField()
    tags = UseCaseTagSerializer(many=True, read_only=True)

    class Meta:
        model = UseCaseFeature
        fields = [
            "id",
            "title",
            "description",
            "image_url",
            "tags",
            "order",
            "is_active",
        ]
        read_only_fields = ["id"]

    def get_image_url(self, obj):
        """Return absolute URL for feature image if present."""
        if not obj.image:
            return None
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url) if request else obj.image.url
