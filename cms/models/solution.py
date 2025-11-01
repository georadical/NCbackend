"""
Solution – NexusCouncil CMS

EN: Represents a core solution or module offered by NexusCouncil (e.g., Urban Planning, Environmental Services).
ES: Representa una solución o módulo principal ofrecido por NexusCouncil (p. ej., Planificación Urbana, Servicios Ambientales).
"""

from django.db import models


class Solution(models.Model):
    """Core solution displayed in the 'A Single Hub for All Your Council's Needs' section."""

    icon = models.CharField(
        max_length=60,
        help_text="Material icon name (e.g., 'map', 'engineering', 'emergency_home').",
    )
    title = models.CharField(max_length=150, help_text="Solution title.")
    description = models.TextField(help_text="Short description of what this solution offers.")
    order = models.PositiveIntegerField(default=0, help_text="Display order on the frontend.")
    is_active = models.BooleanField(default=True, help_text="Controls visibility on the site.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Solution"
        verbose_name_plural = "Solutions"

    def __str__(self):
        return self.title
