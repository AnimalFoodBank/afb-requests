"""
URL configuration for afb project.

"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from rest_framework.authtoken.views import obtain_auth_token

from afbcore.views import users, public
from afbcore.contrib.api_router import APIRouter
from .extra_api_views import EXTRA_API_VIEWS

"""

In settings:
REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'ALLOWED_VERSIONS': ['v1', 'v2'],
    'VERSION_PARAM': 'version'
}

Then in here:
from django.urls import include, path
from . import views

urlpatterns = [
    path('api/<str:version>/users/', include([
        path('', views.UserList.as_view(), name='user-list'),
        path('<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    ])),
]

"""
router = APIRouter(singleViews=EXTRA_API_VIEWS)
router.register(r"users", users.UserViewSet, basename="user")

# TODO: How to add to browsable API?
passwordless = include("drfpasswordless.urls")

# TODO: Prefix with /version
urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("api/", include(router.urls)),
    path("api/passwordless/", passwordless),
    # Add DRF API registration endpoints. We need these for the browsable API.
    # path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),
    # Add drf_registration (package) endpoints. These are used for login, registration,
    # etc from the frontend.
    # path("api/accounts/", include("drf_registration.urls")),
]

urlpatterns.extend(  # TODO: remove
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
