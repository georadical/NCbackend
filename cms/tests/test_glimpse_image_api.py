"""
test_glimpse_image_api – NexusCouncil CMS

EN: Tests the /cms/glimpse-images/ endpoint to ensure active images are returned correctly and ordered for the “A Glimpse of the Platform” section.
ES: Prueba el endpoint /cms/glimpse-images/ para asegurar que las imágenes activas se retornen correctamente y ordenadas para la sección “Una mirada a la plataforma”.
"""

import pytest
from rest_framework.test import APIClient

from cms.models.glimpse_image import GlimpseImage


@pytest.mark.django_db
class TestGlimpseImageAPI:
    """Tests for GlimpseImage API endpoints."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def glimpse_images(self):
        """Create sample images for testing."""
        GlimpseImage.objects.create(
            image="glimpse/dashboard.jpg",
            title="Main Dashboard",
            caption="Overview of council performance metrics.",
            order=1,
            is_active=True,
        )
        GlimpseImage.objects.create(
            image="glimpse/analytics.jpg",
            title="Data Analytics",
            caption="Advanced data insights and visualizations.",
            order=2,
            is_active=True,
        )
        GlimpseImage.objects.create(
            image="glimpse/old_image.jpg",
            title="Legacy View",
            caption="Should not appear.",
            order=3,
            is_active=False,
        )

    def test_list_returns_active_images(self, api_client, glimpse_images):
        """Should return only active GlimpseImage records."""
        response = api_client.get("/cms/glimpse-images/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 2
        titles = [img["title"] for img in data]
        assert "Main Dashboard" in titles
        assert "Data Analytics" in titles
        assert "Legacy View" not in titles

    def test_images_are_ordered(self, api_client, glimpse_images):
        """Images should be ordered ascending by 'order'."""
        response = api_client.get("/cms/glimpse-images/")
        data = response.json()
        orders = [img["order"] for img in data]
        assert orders == sorted(orders)

    def test_each_image_has_required_fields(self, api_client, glimpse_images):
        """Validate image response fields."""
        response = api_client.get("/cms/glimpse-images/")
        data = response.json()[0]
        for field in ["id", "image_url", "title", "caption", "order", "is_active"]:
            assert field in data
