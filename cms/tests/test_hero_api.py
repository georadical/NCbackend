"""
test_hero_api – NexusCouncil CMS

EN: Tests the /cms/hero/ endpoints to ensure the active hero section is returned with valid structure and fields.
ES: Prueba los endpoints /cms/hero/ para asegurar que la sección hero activa se retorne con estructura y campos válidos.
"""

import pytest
from rest_framework.test import APIClient

from cms.models.hero import Hero


@pytest.mark.django_db
class TestHeroAPI:
    """Tests for Hero API endpoints."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def active_hero(self):
        """Create an active Hero instance for testing."""
        return Hero.objects.create(
            title="One GIS-Powered Console for Smarter Councils.",
            subtitle="NexusCouncil centralizes geospatial data and unlocks actionable insights.",
            cta_primary_label="Book a Demo",
            cta_primary_href="#demo",
            cta_secondary_label="See Live Sandbox",
            cta_secondary_href="#sandbox",
            bg_type="pattern",
            is_active=True,
        )

    def test_list_returns_200(self, api_client, active_hero):
        """Should return status 200 and list of Hero sections."""
        response = api_client.get("/cms/hero/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 1
        assert data[0]["title"] == active_hero.title

    def test_get_active_returns_hero(self, api_client, active_hero):
        """Should return active Hero via /cms/hero/active/."""
        response = api_client.get("/cms/hero/active/")
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == active_hero.title
        assert data["cta_primary_label"] == "Book a Demo"
        assert data["bg_type"] == "pattern"

    def test_get_active_returns_404_if_none(self, api_client):
        """Should return 404 if no active Hero exists."""
        response = api_client.get("/cms/hero/active/")
        assert response.status_code == 404
        assert response.json()["detail"] == "No active hero found."
