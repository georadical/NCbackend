"""
Testimonial – NexusCouncil CMS

EN: Represents a client testimonial shown in the “Trusted by Civic Leaders” section, including author details and key impact metrics.
ES: Representa un testimonio de cliente mostrado en la sección “Confiado por líderes cívicos”, incluyendo detalles del autor y métricas clave de impacto.
"""

from django.db import models


class Testimonial(models.Model):
    """Customer testimonial with author information and key metrics."""
    __test__ = False
    quote = models.TextField(help_text="Quoted testimonial text.")
    author_name = models.CharField(max_length=100, help_text="Full name of the testimonial author.")
    author_title = models.CharField(max_length=150, help_text="Author’s title or role (e.g., 'City Planner').")
    organization = models.CharField(max_length=150, help_text="Name of the organization or department.")
    author_photo = models.ImageField(
        upload_to="testimonials/", blank=True, null=True, help_text="Optional author photo."
    )
    verified = models.BooleanField(default=True, help_text="Mark if testimonial is verified.")
    stat_1_label = models.CharField(
        max_length=50, blank=True, help_text="Optional label for the first impact metric (e.g., 'Faster Reviews')."
    )
    stat_1_value = models.CharField(
        max_length=50, blank=True, help_text="Numeric/statistical value for the first metric (e.g., '50%')."
    )
    stat_2_label = models.CharField(
        max_length=50, blank=True, help_text="Optional label for the second impact metric (e.g., 'Productivity Boost')."
    )
    stat_2_value = models.CharField(
        max_length=50, blank=True, help_text="Numeric/statistical value for the second metric (e.g., '20%')."
    )
    order = models.PositiveIntegerField(default=0, help_text="Display order in the frontend.")
    is_active = models.BooleanField(default=True, help_text="Controls visibility on the landing page.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return f"{self.author_name} – {self.organization}"
