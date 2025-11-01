"""
Integration – NexusCouncil CMS

EN: Represents third-party integrations shown in the “Seamlessly Integrated” section, such as Esri, Salesforce, and Microsoft 365.
ES: Representa las integraciones de terceros mostradas en la sección “Integración sin esfuerzo”, como Esri, Salesforce y Microsoft 365.
"""

from django.db import models


class Integration(models.Model):
    """Third-party platform integration item."""

    name = models.CharField(max_length=100, help_text="Integration name (e.g., 'Esri', 'Salesforce').")
    logo = models.ImageField(upload_to="integrations/", help_text="Logo image representing the integration.")
    website_url = models.URLField(blank=True, help_text="Optional URL to the partner or product page.")
    order = models.PositiveIntegerField(default=0, help_text="Display order in the integrations grid.")
    is_active = models.BooleanField(default=True, help_text="Controls whether this integration is visible.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "Integration"
        verbose_name_plural = "Integrations"

    def __str__(self):
        return self.name
