"""
test_site_settings_api – NexusCouncil CMS

EN: Tests the /cms/site-settings/ endpoint to ensure it returns the active SiteSettings instance correctly.
ES: Prueba el endpoint /cms/site-settings/ para asegurar que retorna correctamente la instancia activa de SiteSettings.
"""

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from cms.models.sitesettings import SiteSettings


@pytest.mark.django_db
class TestSiteSettingsAPI:
    """Tests for SiteSettings API endpoints."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def site_settings(self):
        return SiteSettings.objects.create(
            site_name="NexusCouncil",
            theme_primary="#00e676",
            theme_bg_light="#ffffff",
            theme_bg_dark="#111111",
            twitter_url="https://twitter.com/nexuscouncil",
            meta_title="Smarter Councils",
            meta_description="Unified GIS-powered solutions for local government.",
        )

    def test_list_returns_200(self, api_client, site_settings):
        """Should return status 200 and at least one SiteSettings instance."""
        url = reverse("site-settings-list")
        response = api_client.get(url)
        assert response.status_code == 200
        payload = response.json()
        assert isinstance(payload, list)
        assert payload[0]["site_name"] == "NexusCouncil"

    def test_get_active_returns_instance(self, api_client, site_settings):
        """Should return the first active SiteSettings instance via /cms/site-settings/active/."""
        url = reverse("site-settings-get-active")
        response = api_client.get(url)
        assert response.status_code == 200
        data = response.json()
        assert data["site_name"] == "NexusCouncil"
        assert data["theme_primary"] == "#00e676"
