"""
Hero – NexusCouncil CMS

EN: Represents the main hero section of the landing page, including title, subtitle, call-to-actions, and background configuration.
ES: Representa la sección principal (hero) de la página de inicio, incluyendo título, subtítulo, llamados a la acción y configuración del fondo.
"""

from django.db import models


class Hero(models.Model):
    """Main hero section for the landing page."""

    BG_CHOICES = [
        ("pattern", "Subtle Pattern"),
        ("image", "Background Image"),
        ("solid", "Solid Color"),
    ]

    title = models.CharField(max_length=200, default="One GIS-Powered Console for Smarter Councils.")
    subtitle = models.TextField(blank=True, help_text="Optional supporting text below the title.")
    cta_primary_label = models.CharField(max_length=60, default="Book a Demo")
    cta_primary_href = models.CharField(max_length=255, default="#")
    cta_secondary_label = models.CharField(max_length=60, blank=True, default="See Live Sandbox")
    cta_secondary_href = models.CharField(max_length=255, blank=True, default="#")
    bg_type = models.CharField(max_length=20, choices=BG_CHOICES, default="pattern")
    bg_media = models.ImageField(upload_to="hero/", blank=True, null=True, help_text="Optional background image.")
    is_active = models.BooleanField(default=True, help_text="Only one hero should be active at a time.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Sections"

    def __str__(self):
        return f"Hero: {self.title[:50]}"
