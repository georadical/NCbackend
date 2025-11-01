"""
CaseStudySerializer – NexusCouncil CMS

EN: Serializes real-world case studies that highlight measurable community impacts achieved with NexusCouncil.
ES: Serializa los casos de estudio reales que destacan los impactos medibles logrados por las comunidades con NexusCouncil.
"""

from rest_framework import serializers

from cms.models.case_study import CaseStudy


class CaseStudySerializer(serializers.ModelSerializer):
    """Serializer for the CaseStudy model."""

    image_url = serializers.SerializerMethodField()

    class Meta:
        model = CaseStudy
        fields = [
            "id",
            "image_url",
            "category",
            "city",
            "title",
            "summary",
            "order",
            "is_active",
        ]
        read_only_fields = ["id"]

    def get_image_url(self, obj):
        """Return absolute URL for case study image if present."""
        request = self.context.get("request")
        if request and obj.image:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url if obj.image else None
