"""
test_pricing_plan_api – NexusCouncil CMS

EN: Tests the /cms/pricing-plans/ endpoint to ensure active pricing plans are returned correctly for the “Simple, Transparent Pricing” section.
ES: Prueba el endpoint /cms/pricing-plans/ para asegurar que los planes de precios activos se retornen correctamente para la sección “Precios simples y transparentes”.
"""

import pytest
from rest_framework.test import APIClient

from cms.models.pricing_plan import PricingPlan


@pytest.mark.django_db
class TestPricingPlanAPI:
    """Tests for PricingPlan API endpoints."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def pricing_plans(self):
        """Create sample pricing plans for testing."""
        PricingPlan.objects.create(
            name="essentials",
            description="For small towns and councils getting started.",
            price="$499/mo",
            highlight=False,
            order=1,
            features=["Core Mapping & Visualization", "Up to 10 Users", "Community Support"],
            is_active=True,
        )
        PricingPlan.objects.create(
            name="professional",
            description="For growing cities and districts.",
            price="$999/mo",
            highlight=True,
            order=2,
            features=["Advanced Analytics", "Priority Support", "Up to 50 Users"],
            is_active=True,
        )
        PricingPlan.objects.create(
            name="enterprise",
            description="For large cities and regional authorities.",
            price="Contact Us",
            highlight=False,
            order=3,
            features=["Unlimited Users", "API Access", "Dedicated Account Manager"],
            is_active=False,
        )

    def test_list_returns_only_active_plans(self, api_client, pricing_plans):
        """Should return only active PricingPlan records."""
        response = api_client.get("/cms/pricing-plans/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 2
        names = [p["name"] for p in data]
        assert "essentials" in names
        assert "professional" in names
        assert "enterprise" not in names

    def test_pricing_plans_are_ordered(self, api_client, pricing_plans):
        """Plans should be ordered ascending by 'order'."""
        response = api_client.get("/cms/pricing-plans/")
        data = response.json()
        orders = [p["order"] for p in data]
        assert orders == sorted(orders)

    def test_plan_fields_and_features(self, api_client, pricing_plans):
        """Each plan should include required fields and a list of features."""
        response = api_client.get("/cms/pricing-plans/")
        item = response.json()[0]
        for field in ["id", "name", "description", "price", "highlight", "order", "features", "is_active"]:
            assert field in item
        assert isinstance(item["features"], list)

    def test_highlight_flag_present(self, api_client, pricing_plans):
        """Ensure that the highlight flag is returned and correct."""
        response = api_client.get("/cms/pricing-plans/")
        data = response.json()
        highlights = [p["highlight"] for p in data]
        assert any(highlights)
