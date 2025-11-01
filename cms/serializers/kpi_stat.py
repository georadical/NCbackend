"""
KPIStatSerializer – NexusCouncil CMS

EN: Serializes KPI metrics (label, value, order) for display on the landing page.
ES: Serializa las métricas KPI (etiqueta, valor, orden) para mostrarlas en la página de inicio.
"""

from rest_framework import serializers

from cms.models.kpi_stat import KPIStat


class KPIStatSerializer(serializers.ModelSerializer):
    """Serializer for the KPIStat model."""

    class Meta:
        model = KPIStat
        fields = ["id", "label", "value", "order", "is_active"]
        read_only_fields = ["id"]
