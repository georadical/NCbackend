"""
test_case_study_api – NexusCouncil CMS

EN: Tests the /cms/case-studies/ endpoint to ensure case studies are returned correctly for the “Proven Impact for Communities” section.
ES: Prueba el endpoint /cms/case-studies/ para asegurar que los casos de estudio se retornen correctamente para la sección “Impacto comprobado”.
"""

import pytest
from rest_framework.test import APIClient

from cms.models.case_study import CaseStudy


@pytest.mark.django_db
class TestCaseStudyAPI:
    """Tests for CaseStudy API endpoints."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def case_studies(self, tmp_path):
        """Seed active and inactive case studies for list tests."""

        # Active 1
        CaseStudy.objects.create(
            image="case_studies/city1.jpg",
            category="Traffic Flow",
            city="Metropolis",
            title="20% Congestion Reduction",
            summary="Optimized traffic signals based on real-time data.",
            order=1,
            is_active=True,
        )
        # Active 2
        CaseStudy.objects.create(
            image="case_studies/city2.jpg",
            category="Public Safety",
            city="Coastal City",
            title="3-Minute Faster Response",
            summary="Identified high-risk zones and optimized patrol routes.",
            order=2,
            is_active=True,
        )
        # Inactive
        CaseStudy.objects.create(
            image="case_studies/old.jpg",
            category="Infrastructure",
            city="Rivertown",
            title="Legacy project",
            summary="Should not appear.",
            order=3,
            is_active=False,
        )

    def test_list_returns_only_active_case_studies(self, api_client, case_studies):
        response = api_client.get("/cms/case-studies/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 2
        titles = [c["title"] for c in data]
        assert "20% Congestion Reduction" in titles
        assert "3-Minute Faster Response" in titles
        assert "Legacy project" not in titles

    def test_case_studies_are_ordered(self, api_client, case_studies):
        response = api_client.get("/cms/case-studies/")
        data = response.json()
        orders = [c["order"] for c in data]
        assert orders == sorted(orders)

    def test_case_study_has_required_fields(self, api_client, case_studies):
        response = api_client.get("/cms/case-studies/")
        item = response.json()[0]
        for field in ["id", "image_url", "category", "city", "title", "summary", "order", "is_active"]:
            assert field in item
