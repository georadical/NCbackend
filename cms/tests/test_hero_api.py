"""
test_hero_api – NexusCouncil CMS

EN: Tests the /cms/hero/ endpoints to ensure the active hero section is returned with valid structure and fields.
ES: Prueba los endpoints /cms/hero/ para asegurar que la sección hero activa se retorne con estructura y campos válidos.
"""

import pytest
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient

from cms.models.hero import Hero


@pytest.mark.django_db
class TestHeroAPI:
    """Tests for Hero API endpoints."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def staff_user(self):
        """Create a staff user capable of authenticating API requests."""
        """Crea un usuario de staff capaz de autenticar solicitudes API."""
        User = get_user_model()
        return User.objects.create_user(
            username="cms_staff",
            email="staff@example.com",
            password="password123",
            is_staff=True,
        )

    @pytest.fixture
    def auth_client(self, api_client, staff_user):
        """Return API client authenticated as staff user."""
        """Devuelve un cliente API autenticado como usuario de staff."""
        api_client.force_authenticate(user=staff_user)
        return api_client

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

    def test_create_requires_authentication(self, api_client):
        """Should reject unauthenticated creation attempts."""
        """Debe rechazar intentos de creación no autenticados."""
        response = api_client.post(
            "/cms/hero/",
            {
                "title": "New Hero",
                "subtitle": "Auth required.",
                "cta_primary_label": "Start",
                "cta_primary_href": "#start",
                "bg_type": "pattern",
            },
            format="json",
        )
        assert response.status_code == 401

    def test_create_active_hero_deactivates_previous(self, auth_client, active_hero):
        """Should deactivate other heroes when creating a new active hero."""
        """Debe desactivar otros héroes al crear uno nuevo activo."""
        payload = {
            "title": "Fresh Council Insights",
            "subtitle": "All metrics in one dashboard.",
            "cta_primary_label": "Explore",
            "cta_primary_href": "#explore",
            "cta_secondary_label": "Contact Us",
            "cta_secondary_href": "#contact",
            "bg_type": "pattern",
            "is_active": True,
        }
        response = auth_client.post("/cms/hero/", payload, format="json")
        assert response.status_code == 201
        data = response.json()
        assert data["is_active"] is True
        active_hero.refresh_from_db()
        assert active_hero.is_active is False
        assert Hero.objects.filter(is_active=True).count() == 1

    def test_create_image_hero_requires_media(self, auth_client):
        """Should enforce providing bg_media when bg_type is image."""
        """Debe exigir bg_media cuando bg_type es image."""
        response = auth_client.post(
            "/cms/hero/",
            {
                "title": "Visual Hero",
                "subtitle": "With imagery.",
                "cta_primary_label": "View",
                "cta_primary_href": "#view",
                "bg_type": "image",
            },
            format="multipart",
        )
        assert response.status_code == 400
        assert "bg_media" in response.json()

        image_bytes = (
            b"GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00"
            b"\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00"
            b"\x01\x00\x01\x00\x00\x02\x02D\x01\x00;"
        )
        image_content = SimpleUploadedFile(
            "hero.gif",
            content=image_bytes,
            content_type="image/gif",
        )
        response = auth_client.post(
            "/cms/hero/",
            {
                "title": "Visual Hero",
                "subtitle": "With imagery.",
                "cta_primary_label": "View",
                "cta_primary_href": "#view",
                "bg_type": "image",
                "bg_media": image_content,
            },
            format="multipart",
        )
        assert response.status_code == 201
        assert Hero.objects.filter(is_active=True).count() == 1
