"""
SolutionSerializer – NexusCouncil CMS

EN: Serializes NexusCouncil solutions for the landing page hub section.
ES: Serializa las soluciones de NexusCouncil para la sección principal del sitio.
"""

from rest_framework import serializers

from cms.models.solution import Solution


class SolutionSerializer(serializers.ModelSerializer):
    """Serializer for the Solution model."""

    class Meta:
        model = Solution
        fields = ["id", "icon", "title", "description", "order", "is_active"]
        read_only_fields = ["id"]
