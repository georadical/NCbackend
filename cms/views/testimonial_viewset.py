"""
TestimonialViewSet – NexusCouncil CMS

EN: Read-only ViewSet exposing client testimonials for the “Trusted by Civic Leaders” section.
ES: ViewSet de solo lectura que expone los testimonios de clientes en la sección “Confiado por líderes cívicos”.
"""

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from cms.models.testimonial import Testimonial
from cms.serializers.testimonial import TestimonialSerializer


class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only API for Testimonial model."""

    queryset = Testimonial.objects.filter(is_active=True).order_by("order")
    serializer_class = TestimonialSerializer
    permission_classes = [AllowAny]
