"""
test_trust_logo_api – NexusCouncil CMS

EN: Tests the /cms/trust-logos/ endpoint to ensure active logos are returned correctly and in the expected order.
ES: Prueba el endpoint /cms/trust-logos/ para asegurar que los logotipos activos se retornen correctamente y en el orden esperado.
"""

import pytest
from rest_framework.test import APIClient

from cms.models.trust_logo import TrustLogo


@pytest.mark.django_db
class TestTrustLogoAPI:
    """Tests for TrustLogo API endpoints."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def sample_logos(self):
        """Create sample logos for testing."""
        TrustLogo.objects.create(name="City of Metropolis", order=1, is_active=True)
        TrustLogo.objects.create(name="Coastal Council", order=2, is_active=True)
        TrustLogo.objects.create(name="Old City", order=3, is_active=False)  # inactive
        return TrustLogo.objects.all()

    def test_list_returns_active_logos(self, api_client, sample_logos):
        """Should return only active logos with status 200."""
        response = api_client.get("/cms/trust-logos/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 2  # only active ones
        names = [logo["name"] for logo in data]
        assert "City of Metropolis" in names
        assert "Coastal Council" in names
        assert "Old City" not in names

    def test_logos_are_ordered_by_order_field(self, api_client, sample_logos):
        """Logos should be ordered ascending by 'order' field."""
        response = api_client.get("/cms/trust-logos/")
        data = response.json()
        orders = [logo["order"] for logo in data]
        assert orders == sorted(orders)
