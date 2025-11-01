"""
PricingFeature – NexusCouncil CMS

EN: Represents a feature included in a pricing plan, such as “Core Mapping & Visualization” or “Priority Support”.
ES: Representa una característica incluida en un plan de precios, como “Visualización y mapeo básico” o “Soporte prioritario”.
"""

from django.db import models

from cms.models.pricing_plan import PricingPlan


class PricingFeature(models.Model):
    """Feature or benefit associated with a pricing plan."""

    plan = models.ForeignKey(
        PricingPlan,
        on_delete=models.CASCADE,
        related_name="plan_features",
        help_text="The pricing plan this feature belongs to.",
    )
    description = models.CharField(max_length=255, help_text="Short description of the feature.")
    order = models.PositiveIntegerField(default=0, help_text="Display order within the plan.")
    included = models.BooleanField(default=True, help_text="Indicates if the feature is included or optional.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["plan", "order"]
        verbose_name = "Pricing Feature"
        verbose_name_plural = "Pricing Features"

    def __str__(self):
        return f"{self.plan.name} – {self.description}"
