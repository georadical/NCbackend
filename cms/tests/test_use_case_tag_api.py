"""
test_use_case_tag_api – NexusCouncil CMS

EN: Tests the /cms/use-case-tags/ endpoint to ensure active tags are returned correctly and ordered.
ES: Prueba el endpoint /cms/use-case-tags/ para asegurar que las etiquetas activas se retornen correctamente y en orden.
"""

import pytest
from rest_framework.test import APIClient

from cms.models.use_case_tag import UseCaseTag


@pytest.mark.django_db
class TestUseCaseTagAPI:
    """Tests for UseCaseTag API endpoints."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def tags(self):
        """Create sample use case tags for testing."""
        UseCaseTag.objects.create(name="Permit Management", slug="permit-management", order=1, is_active=True)
        UseCaseTag.objects.create(name="Code Enforcement", slug="code-enforcement", order=2, is_active=True)
        UseCaseTag.objects.create(name="Citizen Request Portal", slug="citizen-portal", order=3, is_active=False)
        return UseCaseTag.objects.all()

    def test_list_returns_active_tags(self, api_client, tags):
        """Should return only active use case tags."""
        response = api_client.get("/cms/use-case-tags/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 2
        names = [item["name"] for item in data]
        assert "Permit Management" in names
        assert "Code Enforcement" in names
        assert "Citizen Request Portal" not in names

    def test_tags_are_ordered(self, api_client, tags):
        """Tags should be ordered ascending by 'order' field."""
        response = api_client.get("/cms/use-case-tags/")
        data = response.json()
        orders = [item["order"] for item in data]
        assert orders == sorted(orders)
