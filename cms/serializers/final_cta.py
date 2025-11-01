"""
FinalCTASerializer – NexusCouncil CMS

EN: Serializes the final call-to-action (CTA) section, including main heading, supporting text, and button details.
ES: Serializa la sección final de llamado a la acción (CTA), incluyendo el título principal, texto de apoyo y detalles de los botones.
"""

from rest_framework import serializers

from cms.models.final_cta import FinalCTA


class FinalCTASerializer(serializers.ModelSerializer):
    """Serializer for the FinalCTA model."""

    class Meta:
        model = FinalCTA
        fields = [
            "id",
            "heading",
            "subheading",
            "primary_button_text",
            "primary_button_url",
            "secondary_button_text",
            "secondary_button_url",
            "order",
            "is_active",
        ]
        read_only_fields = ["id"]
