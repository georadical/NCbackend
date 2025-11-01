"""
test_integration_api – NexusCouncil CMS

EN: Tests the /cms/integrations/ endpoint to ensure active integrations are returned correctly and ordered.
ES: Prueba el endpoint /cms/integrations/ para asegurar que las integraciones activas se retornen correctamente y ordenadas.
"""

import pytest
from rest_framework.test import APIClient

from cms.models.integration import Integration


@pytest.mark.django_db
class TestIntegrationAPI:
    """Tests for Integration API endpoints."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def integrations(self):
        """Create sample integration entries for testing."""
        Integration.objects.create(
            name="Esri",
            logo="integrations/esri.png",
            website_url="https://www.esri.com",
            order=1,
            is_active=True,
        )
        Integration.objects.create(
            name="Salesforce",
            logo="integrations/salesforce.png",
            website_url="https://www.salesforce.com",
            order=2,
            is_active=True,
        )
        Integration.objects.create(
            name="OldSystem",
            logo="integrations/old.png",
            website_url="https://old.example.com",
            order=3,
            is_active=False,
        )

    def test_list_returns_only_active_integrations(self, api_client, integrations):
        """Should return only active Integration records."""
        response = api_client.get("/cms/integrations/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 2
        names = [i["name"] for i in data]
        assert "Esri" in names
        assert "Salesforce" in names
        assert "OldSystem" not in names

    def test_integrations_are_ordered(self, api_client, integrations):
        """Integrations should be ordered ascending by 'order'."""
        response = api_client.get("/cms/integrations/")
        data = response.json()
        orders = [i["order"] for i in data]
        assert orders == sorted(orders)

    def test_integration_has_required_fields(self, api_client, integrations):
        """Validate response fields for each integration."""
        response = api_client.get("/cms/integrations/")
        item = response.json()[0]
        for field in ["id", "name", "logo_url", "website_url", "order", "is_active"]:
            assert field in item
