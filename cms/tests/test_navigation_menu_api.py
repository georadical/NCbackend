"""
test_navigation_menu_api – NexusCouncil CMS

EN: Tests the /cms/navigation-menu/ endpoints to ensure header and footer menus are returned correctly.
ES: Prueba los endpoints /cms/navigation-menu/ para asegurar que los menús de encabezado y pie se retornen correctamente.
"""

import pytest
from rest_framework.test import APIClient

from cms.models.navigation_menu import NavigationMenu, NavItem


@pytest.mark.django_db
class TestNavigationMenuAPI:
    """Tests for NavigationMenu API endpoints."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def header_menu(self):
        menu = NavigationMenu.objects.create(name="Main Header", placement="header")
        NavItem.objects.create(menu=menu, label="Home", href="#home", order=1)
        NavItem.objects.create(menu=menu, label="Solutions", href="#solutions", order=2)
        return menu

    @pytest.fixture
    def footer_menu(self):
        menu = NavigationMenu.objects.create(name="Main Footer", placement="footer")
        NavItem.objects.create(menu=menu, label="Privacy", href="#privacy", order=1)
        NavItem.objects.create(menu=menu, label="Contact", href="#contact", order=2)
        return menu

    def test_list_returns_all_menus(self, api_client, header_menu, footer_menu):
        """Should return both header and footer menus."""
        response = api_client.get("/cms/navigation-menu/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 2
        assert any(menu["placement"] == "header" for menu in data)
        assert any(menu["placement"] == "footer" for menu in data)

    def test_get_header_returns_header_menu(self, api_client, header_menu):
        """Should return header menu via /cms/navigation-menu/header/."""
        response = api_client.get("/cms/navigation-menu/header/")
        assert response.status_code == 200
        data = response.json()
        assert data["placement"] == "header"
        assert len(data["items"]) == 2

    def test_get_footer_returns_footer_menu(self, api_client, footer_menu):
        """Should return footer menu via /cms/navigation-menu/footer/."""
        response = api_client.get("/cms/navigation-menu/footer/")
        assert response.status_code == 200
        data = response.json()
        assert data["placement"] == "footer"
        assert len(data["items"]) == 2
