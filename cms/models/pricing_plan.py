"""
PricingPlan – NexusCouncil CMS

EN: Represents pricing plans shown in the “Simple, Transparent Pricing” section, including features, price, and tier type.
ES: Representa los planes de precios mostrados en la sección “Precios simples y transparentes”, incluyendo características, precio y tipo de plan.
"""

from django.db import models


class PricingPlan(models.Model):
    """Pricing plan for the NexusCouncil platform."""

    TIER_CHOICES = [
        ("essentials", "Essentials"),
        ("professional", "Professional"),
        ("enterprise", "Enterprise"),
    ]

    name = models.CharField(
        max_length=100,
        choices=TIER_CHOICES,
        unique=True,
        help_text="Plan name or tier (e.g., Essentials, Professional, Enterprise).",
    )
    description = models.CharField(max_length=255, help_text="Short description of the plan’s target audience.")
    price = models.CharField(max_length=50, help_text="Displayed price (e.g., '$499/mo' or 'Contact Us').")
    highlight = models.BooleanField(default=False, help_text="Marks this plan as 'Most Popular'.")
    order = models.PositiveIntegerField(default=0, help_text="Display order for frontend rendering.")
    features = models.JSONField(default=list, help_text="List of included features.")
    is_active = models.BooleanField(default=True, help_text="Controls whether the plan is visible on the pricing section.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Pricing Plan"
        verbose_name_plural = "Pricing Plans"

    def __str__(self):
        return f"{self.get_name_display()} Plan"
