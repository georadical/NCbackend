"""
GlimpseImage – NexusCouncil CMS

EN: Represents screenshots or preview images of the NexusCouncil platform, shown in the “A Glimpse of the Platform” section.
ES: Representa capturas o imágenes de vista previa de la plataforma NexusCouncil, mostradas en la sección “Una mirada a la plataforma”.
"""

from django.db import models


class GlimpseImage(models.Model):
    """Platform screenshot or preview image."""

    image = models.ImageField(upload_to="glimpse/", help_text="Image file showing part of the platform UI.")
    title = models.CharField(max_length=150, blank=True, help_text="Optional short title or label for the image.")
    caption = models.CharField(max_length=250, blank=True, help_text="Optional short caption describing the image.")
    order = models.PositiveIntegerField(default=0, help_text="Display order in the frontend grid.")
    is_active = models.BooleanField(default=True, help_text="Controls visibility on the landing page.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Glimpse Image"
        verbose_name_plural = "Glimpse Images"

    def __str__(self):
        return self.title or f"Glimpse Image {self.id}"
