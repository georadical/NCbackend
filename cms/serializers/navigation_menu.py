"""
NavigationMenuSerializer – NexusCouncil CMS

EN: Serializes navigation menus (header and footer) and their items for the frontend.
ES: Serializa los menús de navegación (encabezado y pie) y sus elementos para el frontend.
"""

from rest_framework import serializers

from cms.models.navigation_menu import NavigationMenu, NavItem


class NavItemSerializer(serializers.ModelSerializer):
    """Serializer for individual navigation items."""

    class Meta:
        model = NavItem
        fields = ["id", "label", "href", "order"]
        read_only_fields = ["id"]


class NavigationMenuSerializer(serializers.ModelSerializer):
    """Serializer for NavigationMenu including its related items."""

    items = NavItemSerializer(many=True, read_only=True)

    class Meta:
        model = NavigationMenu
        fields = ["id", "name", "placement", "items"]
        read_only_fields = ["id"]
