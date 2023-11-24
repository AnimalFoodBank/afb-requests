"""
URL configuration for afb project.

"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from rest_framework.authtoken.views import obtain_auth_token

from afbcore.views import users
from afbcore.contrib.api_router import APIRouter
from .extra_api_views import EXTRA_API_VIEWS

router = APIRouter(singleViews=EXTRA_API_VIEWS)
router.register(r"users", users.UserViewSet)


# TODO: Prefix with /version
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("auth-token/", obtain_auth_token),
    # Add DRF API registration endpoints
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),
    # Add drf_registration endpoints
    path("/api/accounts/", include("drf_registration.urls")),
]
urlpatterns.extend(
    [
        path(route=endpoint["route"], view=endpoint["view"], name=endpoint["name"])
        for endpoint in EXTRA_API_VIEWS
    ]
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]

    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
