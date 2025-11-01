"""
FooterLinkGroup – NexusCouncil CMS

EN: Represents a group of footer links (e.g., Product, Company, Legal) with a title and associated links.
ES: Representa un grupo de enlaces en el pie de página (por ejemplo, Producto, Empresa, Legal) con su título y enlaces asociados.
"""

from django.db import models


class FooterLinkGroup(models.Model):
    """Footer section group containing related links."""

    title = models.CharField(max_length=100, help_text="Title of the footer link group (e.g., 'Product').")
    links = models.JSONField(default=list, help_text="List of link objects, each with 'label' and 'url'.")
    order = models.PositiveIntegerField(default=0, help_text="Display order for footer link groups.")
    is_active = models.BooleanField(default=True, help_text="Controls visibility in the footer.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Footer Link Group"
        verbose_name_plural = "Footer Link Groups"

    def __str__(self):
        return self.title
