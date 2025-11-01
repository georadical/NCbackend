from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("cms/", include("cms.urls")),  # ✅ Integrates CMS routes globally
]

if "django.contrib.admin" in settings.INSTALLED_APPS:
    urlpatterns.insert(0, path("admin/", admin.site.urls))
