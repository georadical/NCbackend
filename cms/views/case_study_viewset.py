"""
CaseStudyViewSet – NexusCouncil CMS

EN: Read-only ViewSet exposing real-world case studies displayed in the “Proven Impact for Communities” section.
ES: ViewSet de solo lectura que expone los casos de estudio mostrados en la sección “Impacto comprobado en las comunidades”.
"""

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from cms.models.case_study import CaseStudy
from cms.serializers.case_study import CaseStudySerializer


class CaseStudyViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only API for CaseStudy model."""

    queryset = CaseStudy.objects.filter(is_active=True).order_by("order")
    serializer_class = CaseStudySerializer
    permission_classes = [AllowAny]
