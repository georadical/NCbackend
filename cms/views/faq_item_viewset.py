"""
FAQItemViewSet – NexusCouncil CMS

EN: Read-only ViewSet exposing frequently asked questions for the “Frequently Asked Questions” section.
ES: ViewSet de solo lectura que expone las preguntas frecuentes para la sección “Preguntas frecuentes”.
"""

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from cms.models.faq_item import FAQItem
from cms.serializers.faq_item import FAQItemSerializer


class FAQItemViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only API for FAQItem model."""

    queryset = FAQItem.objects.filter(is_active=True).order_by("order")
    serializer_class = FAQItemSerializer
    permission_classes = [AllowAny]
