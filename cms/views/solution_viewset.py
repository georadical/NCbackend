"""
SolutionViewSet – NexusCouncil CMS

EN: Read-only ViewSet exposing NexusCouncil solutions for the “A Single Hub for All Your Council's Needs” section.
ES: ViewSet de solo lectura que expone las soluciones de NexusCouncil para la sección “Un solo centro para todas las necesidades del consejo”.
"""

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from cms.models.solution import Solution
from cms.serializers.solution import SolutionSerializer


class SolutionViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only API for Solution model."""

    queryset = Solution.objects.filter(is_active=True).order_by("order")
    serializer_class = SolutionSerializer
    permission_classes = [AllowAny]
