"""
CMS URLs – NexusCouncil

EN: Registers SolutionViewSet and other CMS ViewSets under /cms/.
ES: Registra el ViewSet Solution y otros ViewSets del CMS bajo /cms/.
"""

from rest_framework.routers import DefaultRouter

from cms.views.case_study_viewset import CaseStudyViewSet
from cms.views.faq_item_viewset import FAQItemViewSet
from cms.views.final_cta_viewset import FinalCTAViewSet
from cms.views.footer_link_group_viewset import FooterLinkGroupViewSet
from cms.views.footer_link_viewset import FooterLinkViewSet
from cms.views.glimpse_image_viewset import GlimpseImageViewSet
from cms.views.hero_viewset import HeroViewSet
from cms.views.integration_viewset import IntegrationViewSet
from cms.views.kpi_stat_viewset import KPIStatViewSet
from cms.views.navigation_menu_viewset import NavigationMenuViewSet
from cms.views.pricing_feature_viewset import PricingFeatureViewSet
from cms.views.pricing_plan_viewset import PricingPlanViewSet
from cms.views.site_settings_viewset import SiteSettingsViewSet
from cms.views.solution_viewset import SolutionViewSet
from cms.views.trust_logo_viewset import TrustLogoViewSet
from cms.views.use_case_feature_viewset import UseCaseFeatureViewSet
from cms.views.use_case_tag_viewset import UseCaseTagViewSet
from cms.views.testimonial_viewset import TestimonialViewSet

router = DefaultRouter()
router.register(r"site-settings", SiteSettingsViewSet, basename="site-settings")
router.register(r"navigation-menu", NavigationMenuViewSet, basename="navigation-menu")
router.register(r"hero", HeroViewSet, basename="hero")
router.register(r"trust-logos", TrustLogoViewSet, basename="trust-logos")
router.register(r"kpi-stats", KPIStatViewSet, basename="kpi-stats")
router.register(r"solutions", SolutionViewSet, basename="solutions")
router.register(r"use-case-tags", UseCaseTagViewSet, basename="use-case-tags")
router.register(r"use-case-features", UseCaseFeatureViewSet, basename="use-case-features")
router.register(r"case-studies", CaseStudyViewSet, basename="case-studies")
router.register(r"glimpse-images", GlimpseImageViewSet, basename="glimpse-images")
router.register(r"integrations", IntegrationViewSet, basename="integrations")
router.register(r"pricing-plans", PricingPlanViewSet, basename="pricing-plans")
router.register(r"pricing-features", PricingFeatureViewSet, basename="pricing-features")
router.register(r"testimonials", TestimonialViewSet, basename="testimonials")
router.register(r"faq-items", FAQItemViewSet, basename="faq-items")
router.register(r"final-cta", FinalCTAViewSet, basename="final-cta")
router.register(r"footer-link-groups", FooterLinkGroupViewSet, basename="footer-link-groups")
router.register(r"footer-links", FooterLinkViewSet, basename="footer-links")

urlpatterns = router.urls
