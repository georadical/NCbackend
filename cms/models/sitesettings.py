"""
SiteSettings – NexusCouncil CMS

EN: Global configuration model that defines the site's branding, theme colors, default SEO metadata,
    and social links. Only one instance should exist (singleton pattern enforced via admin).
ES: Configuración global que define la identidad visual, colores del tema, metadatos SEO y redes sociales
    del sitio. Solo debe existir una instancia activa.
"""

from django.db import models


class SiteSettings(models.Model):
    """Global branding, theme and SEO settings."""

    site_name = models.CharField(max_length=120, default="NexusCouncil")
    logo = models.ImageField(upload_to="branding/", blank=True, null=True)

    # Theme colors
    theme_primary = models.CharField(max_length=7, default="#00e676")
    theme_bg_light = models.CharField(max_length=7, default="#ffffff")
    theme_bg_dark = models.CharField(max_length=7, default="#111111")

    # Social media
    twitter_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)

    # Default SEO
    meta_title = models.CharField(max_length=60, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)
    og_image = models.ImageField(upload_to="seo/", blank=True, null=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return f"Site Settings – {self.site_name}"
