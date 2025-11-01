"""
FooterLink – NexusCouncil CMS

EN: Represents a single footer link belonging to a FooterLinkGroup (e.g., “Privacy Policy” under “Legal”).
ES: Representa un enlace individual del pie de página perteneciente a un FooterLinkGroup (por ejemplo, “Política de Privacidad” bajo “Legal”).
"""

from django.db import models

from cms.models.footer_link_group import FooterLinkGroup


class FooterLink(models.Model):
    """Individual footer link associated with a footer group."""

    group = models.ForeignKey(
        FooterLinkGroup,
        related_name="footer_links",
        on_delete=models.CASCADE,
        help_text="Parent link group (e.g., Product, Company, Legal).",
    )
    label = models.CharField(max_length=100, help_text="Link label displayed in the footer (e.g., 'Privacy Policy').")
    url = models.URLField(help_text="URL the footer link points to.")
    order = models.PositiveIntegerField(default=0, help_text="Order within the footer group.")
    is_active = models.BooleanField(default=True, help_text="Controls visibility of this link.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Footer Link"
        verbose_name_plural = "Footer Links"

    def __str__(self):
        return f"{self.label} ({self.group.title})"
