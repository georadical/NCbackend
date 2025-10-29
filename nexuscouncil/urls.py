"""Project-level URL routing for NexusCouncil."""

from django.urls import include, path

# Public API routes
urlpatterns = [
    path("cms/", include("cms.urls")),
]
