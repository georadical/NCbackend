"""
test_pricing_feature_api – NexusCouncil CMS

EN: Tests the /cms/pricing-features/ endpoint to ensure pricing plan features are returned correctly and ordered by plan and feature order.
ES: Prueba el endpoint /cms/pricing-features/ para asegurar que las características de los planes de precios se retornen correctamente y ordenadas por plan y orden de característica.
"""

import pytest
from rest_framework.test import APIClient

from cms.models.pricing_feature import PricingFeature
from cms.models.pricing_plan import PricingPlan


@pytest.mark.django_db
class TestPricingFeatureAPI:
    """Tests for PricingFeature API endpoints."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def setup_pricing_data(self):
        """Create sample pricing plans and features."""
        essentials = PricingPlan.objects.create(
            name="essentials",
            description="Basic tier for small councils.",
            price="$499/mo",
            order=1,
            features=["Basic Analytics", "Community Support"],
            is_active=True,
        )
        professional = PricingPlan.objects.create(
            name="professional",
            description="For growing cities.",
            price="$999/mo",
            order=2,
            features=["Priority Support", "Advanced Analytics"],
            is_active=True,
        )

        PricingFeature.objects.create(plan=essentials, description="Up to 10 Users", order=1)
        PricingFeature.objects.create(plan=essentials, description="Core Mapping", order=2)
        PricingFeature.objects.create(plan=professional, description="Up to 50 Users", order=1)
        PricingFeature.objects.create(plan=professional, description="API Access", order=2)
        PricingFeature.objects.create(plan=professional, description="Legacy Option", order=3, included=False)

    def test_list_returns_all_features(self, api_client, setup_pricing_data):
        """Should return all PricingFeature records."""
        response = api_client.get("/cms/pricing-features/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 5

    def test_features_are_ordered_by_plan_then_order(self, api_client, setup_pricing_data):
        """Features should be sorted first by plan order, then by feature order."""
        response = api_client.get("/cms/pricing-features/")
        data = response.json()
        # Expect essentials features first (plan order 1), then professional (plan order 2)
        plan_orders = [PricingPlan.objects.get(id=feature["plan"]).order for feature in data]
        assert plan_orders == sorted(plan_orders)

        # Within each plan, ensure feature order ascends
        essentials_orders = [f["order"] for f in data if PricingPlan.objects.get(id=f["plan"]).name == "essentials"]
        professional_orders = [f["order"] for f in data if PricingPlan.objects.get(id=f["plan"]).name == "professional"]
        assert essentials_orders == sorted(essentials_orders)
        assert professional_orders == sorted(professional_orders)

    def test_feature_fields_exist(self, api_client, setup_pricing_data):
        """Each feature should include expected fields."""
        response = api_client.get("/cms/pricing-features/")
        item = response.json()[0]
        for field in ["id", "plan", "description", "order", "included"]:
            assert field in item

    def test_included_flag_present(self, api_client, setup_pricing_data):
        """Should include the boolean 'included' flag."""
        response = api_client.get("/cms/pricing-features/")
        data = response.json()
        assert any("included" in feature for feature in data)
