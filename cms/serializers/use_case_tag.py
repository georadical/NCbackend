"""
UseCaseTagSerializer – NexusCouncil CMS

EN: Serializes use case tags that classify and group use cases in the “Solve Real-World Challenges” section.
ES: Serializa las etiquetas de casos de uso que clasifican y agrupan los casos de uso en la sección “Resuelve desafíos reales”.
"""

from rest_framework import serializers

from cms.models.use_case_tag import UseCaseTag


class UseCaseTagSerializer(serializers.ModelSerializer):
    """Serializer for the UseCaseTag model."""

    class Meta:
        model = UseCaseTag
        fields = ["id", "name", "slug", "description", "order", "is_active"]
        read_only_fields = ["id"]
