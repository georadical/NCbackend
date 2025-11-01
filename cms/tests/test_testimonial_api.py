"""
test_testimonial_api – NexusCouncil CMS

EN: Tests the /cms/testimonials/ endpoint to ensure testimonials are returned correctly for the “Trusted by Civic Leaders” section.
ES: Prueba el endpoint /cms/testimonials/ para asegurar que los testimonios se retornen correctamente para la sección “Confiado por líderes cívicos”.
"""

import pytest
from rest_framework.test import APIClient

from cms.models.testimonial import Testimonial


@pytest.mark.django_db
class TestTestimonialAPI:
    """Tests for Testimonial API endpoints."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def testimonials(self):
        """Create example testimonials for testing."""
        Testimonial.objects.create(
            quote="NexusCouncil has been a game-changer for our planning department.",
            author_name="Sarah Chen",
            author_title="City Planner",
            organization="Metropolis Planning Dept.",
            verified=True,
            stat_1_label="Faster Reviews",
            stat_1_value="50%",
            stat_2_label="Productivity Boost",
            stat_2_value="20%",
            order=1,
            is_active=True,
        )
        Testimonial.objects.create(
            quote="The insights from the platform are invaluable for our community.",
            author_name="David Lee",
            author_title="Public Works Director",
            organization="Capital City Development",
            verified=True,
            stat_1_label="Cost Savings",
            stat_1_value="15%",
            stat_2_label="Data Accuracy",
            stat_2_value="95%",
            order=2,
            is_active=True,
        )
        Testimonial.objects.create(
            quote="Inactive testimonial example.",
            author_name="John Doe",
            author_title="Old Client",
            organization="Legacy Council",
            verified=False,
            order=3,
            is_active=False,
        )

    def test_list_returns_only_active_testimonials(self, api_client, testimonials):
        """Should return only active Testimonial records."""
        response = api_client.get("/cms/testimonials/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 2
        names = [t["author_name"] for t in data]
        assert "Sarah Chen" in names
        assert "David Lee" in names
        assert "John Doe" not in names

    def test_testimonials_are_ordered(self, api_client, testimonials):
        """Testimonials should be ordered ascending by 'order'."""
        response = api_client.get("/cms/testimonials/")
        data = response.json()
        orders = [t["order"] for t in data]
        assert orders == sorted(orders)

    def test_testimonial_fields_exist(self, api_client, testimonials):
        """Each testimonial should include expected fields."""
        response = api_client.get("/cms/testimonials/")
        item = response.json()[0]
        required_fields = [
            "id",
            "quote",
            "author_name",
            "author_title",
            "organization",
            "author_photo_url",
            "verified",
            "stat_1_label",
            "stat_1_value",
            "stat_2_label",
            "stat_2_value",
            "order",
            "is_active",
        ]
        for field in required_fields:
            assert field in item

    def test_verified_flag_is_present(self, api_client, testimonials):
        """Ensure that the verified flag is included and accurate."""
        response = api_client.get("/cms/testimonials/")
        data = response.json()
        verified_flags = [t["verified"] for t in data]
        assert all(verified_flags)
