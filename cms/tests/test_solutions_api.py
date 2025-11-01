"""
test_solutions_api – NexusCouncil CMS

EN: Tests the /cms/solutions/ endpoint to ensure all active solutions are returned correctly and ordered.
ES: Prueba el endpoint /cms/solutions/ para asegurar que todas las soluciones activas se retornen correctamente y en orden.
"""

import pytest
from rest_framework.test import APIClient

from cms.models.solution import Solution


@pytest.mark.django_db
class TestSolutionAPI:
    """Tests for Solution API endpoints."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def sample_solutions(self):
        """Create example solutions for testing."""
        Solution.objects.create(
            icon="map",
            title="Urban Planning & Zoning",
            description="Visualize zoning regulations and track projects.",
            order=1,
            is_active=True,
        )
        Solution.objects.create(
            icon="engineering",
            title="Infrastructure Management",
            description="Monitor assets and schedule maintenance.",
            order=2,
            is_active=True,
        )
        Solution.objects.create(
            icon="park",
            title="Environmental Services",
            description="Track compliance and manage green spaces.",
            order=3,
            is_active=False,
        )
        return Solution.objects.all()

    def test_list_returns_active_solutions(self, api_client, sample_solutions):
        """Should return only active solutions."""
        response = api_client.get("/cms/solutions/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 2
        titles = [solution["title"] for solution in data]
        assert "Urban Planning & Zoning" in titles
        assert "Infrastructure Management" in titles
        assert "Environmental Services" not in titles

    def test_solutions_are_ordered(self, api_client, sample_solutions):
        """Solutions should be ordered ascending by 'order'."""
        response = api_client.get("/cms/solutions/")
        data = response.json()
        orders = [solution["order"] for solution in data]
        assert orders == sorted(orders)
