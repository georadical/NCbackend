"""
TrustLogo – NexusCouncil CMS

EN: Represents a partner or client logo displayed in the “Trusted by forward-thinking local governments” section.
ES: Representa un logotipo de socio o cliente mostrado en la sección “Confiado por gobiernos locales visionarios”.
"""

from django.db import models


class TrustLogo(models.Model):
    """Partner or council logo for the Trusted By section."""

    name = models.CharField(max_length=100, help_text="Partner or organization name.")
    image = models.ImageField(upload_to="trust_logos/", help_text="Logo image to display on the landing page.")
    link = models.URLField(blank=True, null=True, help_text="Optional link to the partner’s website.")
    order = models.PositiveIntegerField(default=0, help_text="Display order on the page.")
    is_active = models.BooleanField(default=True, help_text="Controls whether the logo appears on the site.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Trust Logo"
        verbose_name_plural = "Trust Logos"

    def __str__(self):
        return f"{self.name}"
