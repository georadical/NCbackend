"""
UseCaseFeature – NexusCouncil CMS

EN: Represents a specific use case feature shown in the “Solve Real-World Challenges” section, linked to one or more tags.
ES: Representa una funcionalidad o caso de uso específico mostrado en la sección “Resuelve desafíos reales”, vinculado a una o más etiquetas.
"""

from django.db import models

from cms.models.use_case_tag import UseCaseTag


class UseCaseFeature(models.Model):
    """Specific use case feature or example solution."""

    title = models.CharField(
        max_length=150,
        help_text="Feature title (e.g., 'Streamline Permit Approvals').",
    )
    description = models.TextField(help_text="Detailed explanation of how this feature solves a real-world challenge.")
    image = models.ImageField(upload_to="use_cases/", blank=True, null=True, help_text="Optional image illustrating the feature.")
    tags = models.ManyToManyField(
        UseCaseTag,
        related_name="features",
        blank=True,
        help_text="Tags associated with this feature.",
    )
    order = models.PositiveIntegerField(default=0, help_text="Display order on the frontend.")
    is_active = models.BooleanField(default=True, help_text="Controls visibility on the landing page.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Use Case Feature"
        verbose_name_plural = "Use Case Features"

    def __str__(self):
        return self.title
