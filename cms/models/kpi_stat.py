"""
KPIStat – NexusCouncil CMS

EN: Represents a key performance metric shown below the “Trusted by” logos (e.g., Faster Approvals, Cost Reduction).
ES: Representa un indicador clave de rendimiento mostrado debajo de los logotipos de confianza (p. ej., aprobaciones más rápidas, reducción de costos).
"""

from django.db import models


class KPIStat(models.Model):
    """Key performance indicator for landing page metrics."""

    label = models.CharField(max_length=100, help_text="Short description of the KPI (e.g. 'Faster Permit Approvals').")
    value = models.CharField(max_length=50, help_text="Numeric or symbolic KPI value (e.g. '30%', '15M+', '4.9/5').")
    order = models.PositiveIntegerField(default=0, help_text="Display order in the KPI grid.")
    is_active = models.BooleanField(default=True, help_text="Controls whether this KPI is visible.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "KPI Statistic"
        verbose_name_plural = "KPI Statistics"

    def __str__(self):
        return f"{self.value} – {self.label}"
