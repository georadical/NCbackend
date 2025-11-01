"""
CaseStudy – NexusCouncil CMS

EN: Represents a real-world case study highlighting measurable outcomes achieved by councils using NexusCouncil.
ES: Representa un caso de estudio real que muestra resultados medibles logrados por los consejos que usan NexusCouncil.
"""

from django.db import models


class CaseStudy(models.Model):
    """Case study or success story for the 'Proven Impact for Communities' section."""

    image = models.ImageField(upload_to="case_studies/", help_text="Main image illustrating the case study.")
    category = models.CharField(max_length=100, help_text="Category label (e.g., 'Traffic Flow', 'Public Safety').")
    city = models.CharField(max_length=100, help_text="City or organization name (e.g., 'Metropolis').")
    title = models.CharField(max_length=200, help_text="Title summarizing the key outcome (e.g., '20% Congestion Reduction').")
    summary = models.TextField(help_text="Short paragraph describing the results and how they were achieved.")
    order = models.PositiveIntegerField(default=0, help_text="Display order in the grid.")
    is_active = models.BooleanField(default=True, help_text="Controls visibility on the landing page.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Case Study"
        verbose_name_plural = "Case Studies"

    def __str__(self):
        return f"{self.city} – {self.title}"
