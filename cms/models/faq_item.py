"""
FAQItem – NexusCouncil CMS

EN: Represents a frequently asked question and its corresponding answer shown in the “Frequently Asked Questions” section.
ES: Representa una pregunta frecuente y su respectiva respuesta mostrada en la sección “Preguntas frecuentes”.
"""

from django.db import models


class FAQItem(models.Model):
    """Frequently asked question and its answer."""

    question = models.CharField(max_length=255, help_text="The FAQ question text.")
    answer = models.TextField(help_text="The corresponding answer to the FAQ question.")
    order = models.PositiveIntegerField(default=0, help_text="Display order in the FAQ section.")
    is_active = models.BooleanField(default=True, help_text="Controls visibility on the landing page.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "FAQ Item"
        verbose_name_plural = "FAQ Items"

    def __str__(self):
        return self.question
