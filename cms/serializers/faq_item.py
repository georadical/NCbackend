"""
FAQItemSerializer – NexusCouncil CMS

EN: Serializes frequently asked questions and answers for the “Frequently Asked Questions” section.
ES: Serializa las preguntas y respuestas frecuentes para la sección “Preguntas frecuentes”.
"""

from rest_framework import serializers

from cms.models.faq_item import FAQItem


class FAQItemSerializer(serializers.ModelSerializer):
    """Serializer for the FAQItem model."""

    class Meta:
        model = FAQItem
        fields = [
            "id",
            "question",
            "answer",
            "order",
            "is_active",
        ]
        read_only_fields = ["id"]
