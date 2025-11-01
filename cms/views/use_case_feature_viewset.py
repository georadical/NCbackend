"""
UseCaseFeatureViewSet – NexusCouncil CMS

EN: Read-only ViewSet exposing use case features displayed in the “Solve Real-World Challenges” section, including their related tags.
ES: ViewSet de solo lectura que expone las funcionalidades o casos de uso mostrados en la sección “Resuelve desafíos reales”, incluyendo sus etiquetas relacionadas.
"""

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from cms.models.use_case_feature import UseCaseFeature
from cms.serializers.use_case_feature import UseCaseFeatureSerializer


class UseCaseFeatureViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only API for UseCaseFeature model."""

    queryset = (
        UseCaseFeature.objects.filter(is_active=True)
        .prefetch_related("tags")
        .order_by("order")
    )
    serializer_class = UseCaseFeatureSerializer
    permission_classes = [AllowAny]
