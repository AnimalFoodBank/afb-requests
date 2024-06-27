"""
URL configuration for afb project.

"""

from afbcore.views import (
    BranchViewSet,
    FoodRequestViewSet,
    ProfileViewSet,
    authtoken,
    users,
)
from django.conf import settings
from django.contrib import admin as afbcore_admin
from django.urls import include, path
from django.views import defaults as default_views
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

passwordless = include("drfpasswordless.urls")

router = DefaultRouter()

# e.g. /api/v1/requests/abcdef1234/
router.register("requests", FoodRequestViewSet, basename="foodrequest")
router.register("profiles", ProfileViewSet, basename="profile")
router.register("branches", BranchViewSet)

urlpatterns = [
    path("afbadmin/", afbcore_admin.site.urls, name="admin"),
    path(
        "api/<str:version>/register/",
        users.RegisterUserAPIView.as_view(),
        name="registration",
    ),
    path(
        "api/<str:version>/current_user/",
        users.CurrentUserAPIView.as_view(),
        name="current_user",
    ),
    path("api/<str:version>/", include(router.urls)),
    path("api/<str:version>/passwordless/", passwordless),
    path(
        "api/<str:version>/authtoken/auth/",
        obtain_auth_token,
        name="api_token_auth",
    ),
    path(
        "api/<str:version>/authtoken/logout/",
        authtoken.LogoutView.as_view(),
        name="api_token_logout",
    ),
    path(
        "api/<str:version>/schema/", SpectacularAPIView.as_view(), name="schema"
    ),
    path(
        "api/<str:version>/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/<str:version>/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    #
    # TODO: Figure how to respond with JSON or HTML based on request
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

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls))
        ] + urlpatterns
