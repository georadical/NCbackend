"""
CMS URLs – NexusCouncil

EN: Registers SolutionViewSet and other CMS ViewSets under /cms/.
ES: Registra el ViewSet Solution y otros ViewSets del CMS bajo /cms/.
"""

from rest_framework.routers import DefaultRouter

from cms.views.hero_viewset import HeroViewSet
from cms.views.kpi_stat_viewset import KPIStatViewSet
from cms.views.navigation_menu_viewset import NavigationMenuViewSet
from cms.views.site_settings_viewset import SiteSettingsViewSet
from cms.views.solution_viewset import SolutionViewSet
from cms.views.trust_logo_viewset import TrustLogoViewSet
from cms.views.use_case_feature_viewset import UseCaseFeatureViewSet
from cms.views.use_case_tag_viewset import UseCaseTagViewSet

router = DefaultRouter()
router.register(r"site-settings", SiteSettingsViewSet, basename="site-settings")
router.register(r"navigation-menu", NavigationMenuViewSet, basename="navigation-menu")
router.register(r"hero", HeroViewSet, basename="hero")
router.register(r"trust-logos", TrustLogoViewSet, basename="trust-logos")
router.register(r"kpi-stats", KPIStatViewSet, basename="kpi-stats")
router.register(r"solutions", SolutionViewSet, basename="solutions")
router.register(r"use-case-tags", UseCaseTagViewSet, basename="use-case-tags")
router.register(r"use-case-features", UseCaseFeatureViewSet, basename="use-case-features")

urlpatterns = router.urls
