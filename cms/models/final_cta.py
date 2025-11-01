"""
FinalCTA – NexusCouncil CMS

EN: Represents the final call-to-action (CTA) section encouraging users to take action, such as booking a demo or contacting sales.
ES: Representa la sección final de llamado a la acción (CTA) que invita a los usuarios a tomar acción, como reservar una demo o contactar ventas.
"""

from django.db import models


class FinalCTA(models.Model):
    """Final call-to-action section content."""

    heading = models.CharField(
        max_length=200,
        help_text="Main headline for the final CTA (e.g., 'Ready to Build a Smarter Council?').",
    )
    subheading = models.TextField(help_text="Supporting text that elaborates the CTA purpose.")
    primary_button_text = models.CharField(
        max_length=100,
        default="Book Your Free Demo",
        help_text="Text for the main button.",
    )
    primary_button_url = models.URLField(blank=True, help_text="URL the primary button links to.")
    secondary_button_text = models.CharField(
        max_length=100,
        blank=True,
        help_text="Optional text for a secondary button.",
    )
    secondary_button_url = models.URLField(blank=True, help_text="URL the secondary button links to.")
    order = models.PositiveIntegerField(default=0, help_text="Display order if multiple CTAs exist.")
    is_active = models.BooleanField(default=True, help_text="Controls whether this CTA section is visible.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Final CTA"
        verbose_name_plural = "Final CTAs"

    def __str__(self):
        return self.heading
