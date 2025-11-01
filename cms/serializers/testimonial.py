"""
TestimonialSerializer – NexusCouncil CMS

EN: Serializes client testimonials for the “Trusted by Civic Leaders” section, including author details and performance metrics.
ES: Serializa los testimonios de clientes para la sección “Confiado por líderes cívicos”, incluyendo los detalles del autor y métricas de desempeño.
"""

from rest_framework import serializers

from cms.models.testimonial import Testimonial


class TestimonialSerializer(serializers.ModelSerializer):
    """Serializer for the Testimonial model."""

    author_photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Testimonial
        fields = [
            "id",
            "quote",
            "author_name",
            "author_title",
            "organization",
            "author_photo_url",
            "verified",
            "stat_1_label",
            "stat_1_value",
            "stat_2_label",
            "stat_2_value",
            "order",
            "is_active",
        ]
        read_only_fields = ["id"]

    def get_author_photo_url(self, obj):
        """Return absolute URL for author photo if present."""
        request = self.context.get("request")
        if request and obj.author_photo:
            return request.build_absolute_uri(obj.author_photo.url)
        return obj.author_photo.url if obj.author_photo else None
