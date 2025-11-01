"""
UseCaseTagViewSet – NexusCouncil CMS

EN: Read-only ViewSet exposing tags that classify use cases in the “Solve Real-World Challenges” section.
ES: ViewSet de solo lectura que expone las etiquetas que clasifican los casos de uso en la sección “Resuelve desafíos reales”.
"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from cms.models.use_case_tag import UseCaseTag
from cms.serializers.use_case_tag import UseCaseTagSerializer


class UseCaseTagViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only API for UseCaseTag model."""

    queryset = UseCaseTag.objects.filter(is_active=True).order_by("order", "name")
    serializer_class = UseCaseTagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
