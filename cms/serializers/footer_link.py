"""
FooterLinkSerializer – NexusCouncil CMS

EN: Serializes individual footer links belonging to footer link groups.
ES: Serializa los enlaces individuales del pie de página pertenecientes a los grupos de enlaces.
"""

from rest_framework import serializers

from cms.models.footer_link import FooterLink


class FooterLinkSerializer(serializers.ModelSerializer):
    """Serializer for the FooterLink model."""

    class Meta:
        model = FooterLink
        fields = [
            "id",
            "group",
            "label",
            "url",
            "order",
            "is_active",
        ]
        read_only_fields = ["id"]
