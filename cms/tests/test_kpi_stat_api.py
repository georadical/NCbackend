"""
test_kpi_stat_api – NexusCouncil CMS

EN: Tests the /cms/kpi-stats/ endpoint to ensure KPI data is returned correctly and ordered.
ES: Prueba el endpoint /cms/kpi-stats/ para asegurar que los datos KPI se retornen correctamente y en orden.
"""

import pytest
from rest_framework.test import APIClient

from cms.models.kpi_stat import KPIStat


@pytest.mark.django_db
class TestKPIStatAPI:
    """Tests for KPIStat API endpoints."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def kpis(self):
        """Create sample KPIs for testing."""
        KPIStat.objects.create(label="Faster Permit Approvals", value="30%", order=1, is_active=True)
        KPIStat.objects.create(label="Data Points Analyzed", value="15M+", order=2, is_active=True)
        KPIStat.objects.create(label="Field Ops Cost Reduction", value="25%", order=3, is_active=False)
        return KPIStat.objects.all()

    def test_list_returns_active_kpis(self, api_client, kpis):
        """Should return only active KPIs."""
        response = api_client.get("/cms/kpi-stats/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 2  # only active ones
        labels = [kpi["label"] for kpi in data]
        assert "Faster Permit Approvals" in labels
        assert "Data Points Analyzed" in labels
        assert "Field Ops Cost Reduction" not in labels

    def test_kpis_are_ordered(self, api_client, kpis):
        """KPIs should be ordered ascending by 'order'."""
        response = api_client.get("/cms/kpi-stats/")
        data = response.json()
        orders = [kpi["order"] for kpi in data]
        assert orders == sorted(orders)
