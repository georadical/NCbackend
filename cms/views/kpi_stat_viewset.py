"""
KPIStatViewSet – NexusCouncil CMS

EN: Read-only ViewSet exposing key performance indicators (KPIs) for the landing page metrics section.
ES: ViewSet de solo lectura que expone los indicadores clave de rendimiento (KPI) para la sección de métricas de la página de inicio.
"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from cms.models.kpi_stat import KPIStat
from cms.serializers.kpi_stat import KPIStatSerializer


class KPIStatViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only API for KPIStat model."""

    queryset = KPIStat.objects.filter(is_active=True).order_by("order")
    serializer_class = KPIStatSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
