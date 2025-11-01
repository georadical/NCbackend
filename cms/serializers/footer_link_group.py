"""
FooterLinkGroupSerializer – NexusCouncil CMS

EN: Serializes footer link groups and their associated link lists for display in the website footer.
ES: Serializa los grupos de enlaces del pie de página y sus listas asociadas para mostrarlos en el sitio web.
"""

from rest_framework import serializers

from cms.models.footer_link_group import FooterLinkGroup


class FooterLinkGroupSerializer(serializers.ModelSerializer):
    """Serializer for the FooterLinkGroup model."""

    class Meta:
        model = FooterLinkGroup
        fields = [
            "id",
            "title",
            "links",
            "order",
            "is_active",
        ]
        read_only_fields = ["id"]
