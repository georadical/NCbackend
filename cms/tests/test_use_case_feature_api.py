"""
test_use_case_feature_api – NexusCouncil CMS

EN: Tests the /cms/use-case-features/ endpoint to ensure active use case features and their tags are returned correctly and ordered.
ES: Prueba el endpoint /cms/use-case-features/ para asegurar que las funcionalidades activas y sus etiquetas se retornen correctamente y en orden.
"""

import pytest
from rest_framework.test import APIClient

from cms.models.use_case_feature import UseCaseFeature
from cms.models.use_case_tag import UseCaseTag


@pytest.mark.django_db
class TestUseCaseFeatureAPI:
    """Tests for UseCaseFeature API endpoints."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def setup_features(self):
        """Create tags and features for testing."""
        tag1 = UseCaseTag.objects.create(name="Permit Management", slug="permit-management", order=1)
        tag2 = UseCaseTag.objects.create(name="Code Enforcement", slug="code-enforcement", order=2)

        feature_one = UseCaseFeature.objects.create(
            title="Streamline Permit Approvals",
            description="Digitize the entire permit lifecycle and reduce paperwork.",
            order=1,
            is_active=True,
        )
        feature_one.tags.add(tag1)

        feature_two = UseCaseFeature.objects.create(
            title="Code Compliance Automation",
            description="Simplify inspections and automate reporting.",
            order=2,
            is_active=True,
        )
        feature_two.tags.add(tag2)

        UseCaseFeature.objects.create(
            title="Inactive Case Example",
            description="This should not appear.",
            order=3,
            is_active=False,
        )

        return [feature_one, feature_two]

    def test_list_returns_active_features(self, api_client, setup_features):
        """Should return only active use case features."""
        response = api_client.get("/cms/use-case-features/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 2
        titles = [feature["title"] for feature in data]
        assert "Streamline Permit Approvals" in titles
        assert "Code Compliance Automation" in titles
        assert "Inactive Case Example" not in titles

    def test_features_include_tags(self, api_client, setup_features):
        """Each feature should include its related tags."""
        response = api_client.get("/cms/use-case-features/")
        data = response.json()
        assert len(data[0]["tags"]) >= 1
        assert all("name" in tag for feature in data for tag in feature["tags"])

    def test_features_are_ordered(self, api_client, setup_features):
        """Features should be ordered ascending by 'order'."""
        response = api_client.get("/cms/use-case-features/")
        data = response.json()
        orders = [feature["order"] for feature in data]
        assert orders == sorted(orders)
