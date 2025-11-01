"""
test_footer_link_group_api – NexusCouncil CMS

EN: Tests the /cms/footer-link-groups/ endpoint to ensure footer link groups are returned correctly for the site footer.
ES: Prueba el endpoint /cms/footer-link-groups/ para asegurar que los grupos de enlaces del pie de página se retornen correctamente.
"""

import pytest
from rest_framework.test import APIClient

from cms.models.footer_link_group import FooterLinkGroup


@pytest.mark.django_db
class TestFooterLinkGroupAPI:
    """Tests for FooterLinkGroup API endpoints."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def footer_groups(self):
        """Create sample footer link groups."""
        FooterLinkGroup.objects.create(
            title="Product",
            links=[
                {"label": "Solutions", "url": "/#solutions"},
                {"label": "Pricing", "url": "/#pricing"},
                {"label": "Book a Demo", "url": "/#demo"},
            ],
            order=1,
            is_active=True,
        )
        FooterLinkGroup.objects.create(
            title="Company",
            links=[
                {"label": "About Us", "url": "/about"},
                {"label": "Careers", "url": "/careers"},
                {"label": "Contact Us", "url": "/contact"},
            ],
            order=2,
            is_active=True,
        )
        FooterLinkGroup.objects.create(
            title="Legacy",
            links=[{"label": "Deprecated", "url": "/deprecated"}],
            order=3,
            is_active=False,
        )

    def test_list_returns_only_active_footer_groups(self, api_client, footer_groups):
        """Should return only active FooterLinkGroup records."""
        response = api_client.get("/cms/footer-link-groups/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 2
        titles = [group["title"] for group in data]
        assert "Product" in titles
        assert "Company" in titles
        assert "Legacy" not in titles

    def test_footer_groups_are_ordered(self, api_client, footer_groups):
        """Footer link groups should be ordered ascending by 'order'."""
        response = api_client.get("/cms/footer-link-groups/")
        data = response.json()
        orders = [g["order"] for g in data]
        assert orders == sorted(orders)

    def test_footer_group_structure(self, api_client, footer_groups):
        """Each footer group should include expected fields."""
        response = api_client.get("/cms/footer-link-groups/")
        item = response.json()[0]
        required_fields = ["id", "title", "links", "order", "is_active"]
        for field in required_fields:
            assert field in item
        assert isinstance(item["links"], list)
        assert all("label" in link and "url" in link for link in item["links"])
