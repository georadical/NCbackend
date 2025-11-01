"""
UseCaseTag – NexusCouncil CMS

EN: Represents a category or tag used to classify use cases in the “Solve Real-World Challenges” section.
ES: Representa una categoría o etiqueta utilizada para clasificar los casos de uso en la sección “Resuelve desafíos reales”.
"""

from django.db import models


class UseCaseTag(models.Model):
    """Tag or category for grouping use cases."""

    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Tag name (e.g., 'Permit Management', 'Code Enforcement').",
    )
    slug = models.SlugField(unique=True, max_length=120, help_text="URL-friendly version of the tag name.")
    description = models.TextField(blank=True, help_text="Optional short description for this tag.")
    order = models.PositiveIntegerField(default=0, help_text="Display order for the frontend.")
    is_active = models.BooleanField(default=True, help_text="Controls whether the tag is visible or selectable.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "Use Case Tag"
        verbose_name_plural = "Use Case Tags"

    def __str__(self):
        return self.name
