"""
test_footer_link_api – NexusCouncil CMS

EN: Tests the /cms/footer-links/ endpoint to ensure active footer links are returned correctly and ordered properly.
ES: Prueba el endpoint /cms/footer-links/ para asegurar que los enlaces activos del pie de página se retornen correctamente y en el orden adecuado.
"""

import pytest
from rest_framework.test import APIClient

from cms.models.footer_link import FooterLink
from cms.models.footer_link_group import FooterLinkGroup


@pytest.mark.django_db
class TestFooterLinkAPI:
    """Tests for FooterLink API endpoints."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def footer_links(self):
        """Create sample footer links under different groups."""
        product_group = FooterLinkGroup.objects.create(title="Product", order=1)
        company_group = FooterLinkGroup.objects.create(title="Company", order=2)
        FooterLink.objects.create(group=product_group, label="Solutions", url="/#solutions", order=1, is_active=True)
        FooterLink.objects.create(group=product_group, label="Pricing", url="/#pricing", order=2, is_active=True)
        FooterLink.objects.create(group=company_group, label="About Us", url="/about", order=1, is_active=True)
        FooterLink.objects.create(group=company_group, label="Careers", url="/careers", order=2, is_active=False)

    def test_list_returns_only_active_links(self, api_client, footer_links):
        """Should return only active FooterLink records."""
        response = api_client.get("/cms/footer-links/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 3
        labels = [link["label"] for link in data]
        assert "Solutions" in labels
        assert "Pricing" in labels
        assert "About Us" in labels
        assert "Careers" not in labels

    def test_links_are_ordered_by_group_then_order(self, api_client, footer_links):
        """Ensure footer links are ordered by group and then by link order."""
        response = api_client.get("/cms/footer-links/")
        data = response.json()
        group_orders = dict(FooterLinkGroup.objects.values_list("id", "order"))
        pairs = [(group_orders[link["group"]], link["order"]) for link in data]
        assert pairs == sorted(pairs)

    def test_each_link_has_expected_fields(self, api_client, footer_links):
        """Each footer link should include required fields."""
        response = api_client.get("/cms/footer-links/")
        item = response.json()[0]
        required_fields = ["id", "group", "label", "url", "order", "is_active"]
        for field in required_fields:
            assert field in item
