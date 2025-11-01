"""
test_final_cta_api – NexusCouncil CMS

EN: Tests the /cms/final-cta/ endpoint to ensure the final call-to-action (CTA) section is returned correctly for the landing page.
ES: Prueba el endpoint /cms/final-cta/ para asegurar que la sección final de llamado a la acción (CTA) se retorne correctamente para la página principal.
"""

import pytest
from rest_framework.test import APIClient

from cms.models.final_cta import FinalCTA


@pytest.mark.django_db
class TestFinalCTAAPI:
    """Tests for FinalCTA API endpoints."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def final_ctas(self):
        """Create example FinalCTA entries for testing."""
        FinalCTA.objects.create(
            heading="Ready to Build a Smarter Council?",
            subheading="See how NexusCouncil can transform your operations. Get a personalized demo and a free trial today.",
            primary_button_text="Book Your Free Demo",
            primary_button_url="https://nexuscouncil.com/demo",
            secondary_button_text="Contact Sales",
            secondary_button_url="https://nexuscouncil.com/contact",
            order=1,
            is_active=True,
        )
        FinalCTA.objects.create(
            heading="Legacy CTA Example",
            subheading="This one should not appear because it is inactive.",
            primary_button_text="Learn More",
            order=2,
            is_active=False,
        )

    def test_list_returns_only_active_ctas(self, api_client, final_ctas):
        """Should return only active FinalCTA records."""
        response = api_client.get("/cms/final-cta/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["heading"] == "Ready to Build a Smarter Council?"

    def test_cta_has_required_fields(self, api_client, final_ctas):
        """Each CTA should include expected fields."""
        response = api_client.get("/cms/final-cta/")
        item = response.json()[0]
        required_fields = [
            "id",
            "heading",
            "subheading",
            "primary_button_text",
            "primary_button_url",
            "secondary_button_text",
            "secondary_button_url",
            "order",
            "is_active",
        ]
        for field in required_fields:
            assert field in item

    def test_cta_ordering(self, api_client, final_ctas):
        """Ensure CTAs are ordered by 'order' field."""
        response = api_client.get("/cms/final-cta/")
        data = response.json()
        orders = [cta["order"] for cta in data]
        assert orders == sorted(orders)
