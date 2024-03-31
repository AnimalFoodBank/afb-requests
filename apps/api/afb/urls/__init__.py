"""
URL configuration for afb project.

"""

from django.conf import settings
from django.contrib import admin as afbcore_admin
from django.urls import include, path
from django.views import defaults as default_views
from drfpasswordless import admin as passwordless_admin
from rest_framework.routers import DefaultRouter

from afbcore.views import users, RequestViewSet
from afbcore.contrib.api_router import APIRouter

router = DefaultRouter()
router.register("request", RequestViewSet, basename="request")
router.register(r"users", users.UserViewSet, basename="user")

# TODO: How to add to browsable API?
passwordless = include("drfpasswordless.urls")

# TODO: Prefix with /version
urlpatterns = [
    path("admin/", afbcore_admin.site.urls, name="admin"),
    path("api/", include(router.urls)),
    path("api/passwordless/", passwordless),
]


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
