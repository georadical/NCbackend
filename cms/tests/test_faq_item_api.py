"""
test_faq_item_api – NexusCouncil CMS

EN: Tests the /cms/faq-items/ endpoint to ensure active FAQ entries are returned correctly for the “Frequently Asked Questions” section.
ES: Prueba el endpoint /cms/faq-items/ para asegurar que las preguntas frecuentes activas se retornen correctamente para la sección “Preguntas frecuentes”.
"""

import pytest
from rest_framework.test import APIClient

from cms.models.faq_item import FAQItem


@pytest.mark.django_db
class TestFAQItemAPI:
    """Tests for FAQItem API endpoints."""

    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def faq_items(self):
        """Create sample FAQ items for testing."""
        FAQItem.objects.create(
            question="What kind of data can be imported into NexusCouncil?",
            answer="NexusCouncil supports Shapefiles, GeoJSON, KML, CSVs, and direct ArcGIS connections.",
            order=1,
            is_active=True,
        )
        FAQItem.objects.create(
            question="Is NexusCouncil secure?",
            answer="Yes, we use industry-standard encryption and role-based access controls.",
            order=2,
            is_active=True,
        )
        FAQItem.objects.create(
            question="Is there a mobile app?",
            answer="Yes, NexusCouncil is fully optimized for mobile devices.",
            order=3,
            is_active=False,
        )

    def test_list_returns_only_active_faqs(self, api_client, faq_items):
        """Should return only active FAQItem records."""
        response = api_client.get("/cms/faq-items/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 2
        questions = [f["question"] for f in data]
        assert "What kind of data can be imported into NexusCouncil?" in questions
        assert "Is NexusCouncil secure?" in questions
        assert "Is there a mobile app?" not in questions

    def test_faq_items_are_ordered(self, api_client, faq_items):
        """FAQ items should be ordered ascending by 'order'."""
        response = api_client.get("/cms/faq-items/")
        data = response.json()
        orders = [f["order"] for f in data]
        assert orders == sorted(orders)

    def test_each_faq_has_required_fields(self, api_client, faq_items):
        """Each FAQ item should include expected fields."""
        response = api_client.get("/cms/faq-items/")
        item = response.json()[0]
        for field in ["id", "question", "answer", "order", "is_active"]:
            assert field in item
