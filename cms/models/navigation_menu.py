"""
NavigationMenu – NexusCouncil CMS

EN: Stores menu containers (header, footer) and their ordered links.
ES: Almacena los contenedores de menús (encabezado, pie) y sus enlaces ordenados.
"""

from django.db import models


class NavigationMenu(models.Model):
    """Menu container (header or footer)."""

    PLACEMENT_CHOICES = [
        ("header", "Header"),
        ("footer", "Footer"),
    ]

    name = models.CharField(max_length=100)
    placement = models.CharField(max_length=10, choices=PLACEMENT_CHOICES, default="header")

    def __str__(self):
        return f"{self.name} ({self.placement})"


class NavItem(models.Model):
    """Single link within a navigation menu."""

    menu = models.ForeignKey(NavigationMenu, on_delete=models.CASCADE, related_name="items")
    label = models.CharField(max_length=100)
    href = models.CharField(max_length=255, help_text="URL or hash link (e.g. #solutions)")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Navigation Item"
        verbose_name_plural = "Navigation Items"

    def __str__(self):
        return f"{self.menu.name} → {self.label}"
