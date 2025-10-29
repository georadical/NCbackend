"""
CMS URLs – NexusCouncil

EN: Registers the SiteSettingsViewSet route under /cms/site-settings/.
ES: Registra la ruta del SiteSettingsViewSet bajo /cms/site-settings/.
"""

from rest_framework.routers import DefaultRouter

from cms.views.site_settings_viewset import SiteSettingsViewSet

router = DefaultRouter()
router.register(r"site-settings", SiteSettingsViewSet, basename="site-settings")

# Expose read-only endpoint for site settings data.
urlpatterns = router.urls
