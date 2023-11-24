"""
URL configuration for afb project.

"""

from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from django.views import defaults as default_views

from drf_registration.api.register import ActivateView
from drf_registration.api.change_password import ChangePasswordView
from drf_registration.api.login import LoginView, SocialLoginView
from drf_registration.api.logout import LogoutView
from drf_registration.api.profile import ProfileView
from drf_registration.api.reset_password import (
    ResetPasswordView,
    ResetPasswordConfirmView,
    ResetPasswordCompleteView,
)
from drf_registration.api.set_password import SetPasswordView
from drf_registration.api.register import VerifyView

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

from afbcore.views import users, RegisterView


# Create a router subclassed from DefaultRouter and give it a list[dict] as input
# via: https://github.com/encode/django-rest-framework/discussions/7830#discussioncomment-7205311
class APIRouter(routers.DefaultRouter):
    """
    Customized Default Router to include non-viewset views on root page
    """

    singleViews: list

    def __init__(self, singleViews: list, *args, **kwargs):
        self.singleViews = singleViews
        super().__init__(*args, **kwargs)

    def get_api_root_view(self, api_urls=None):
        """
        Return a basic root view.
        """
        api_root_dict = dict()
        list_name = self.routes[0].name
        for prefix, viewset, basename in self.registry:
            api_root_dict[prefix] = list_name.format(basename=basename)
        for singleView in self.singleViews:
            api_root_dict[singleView["route"]] = singleView["name"]
        return self.APIRootView.as_view(api_root_dict=api_root_dict)


# Define list - replace my_api_view with any view class that subclasses DRF's APIView (including Login, Logout views e.g. django-rest-knox)
singleViews = [
    # e.g. http://127.0.0.1:8000/api/accounts/register/
    {
        "route": "api/accounts/activate/<uidb64>/<token>/",
        "view": ActivateView.as_view(),
        "name": "drf-activate",
    },
    {
        "route": "api/accounts/change-password/",
        "view": ChangePasswordView.as_view(),
        "name": "drf-change_password",
    },
    {
        "route": "api/accounts/login/",
        "view": LoginView.as_view(),
        "name": "drf-login",
    },
    {
        "route": "api/accounts/login/social/",
        "view": SocialLoginView.as_view(),
        "name": "drf-login_social",
    },
    {
        "route": "api/accounts/logout/",
        "view": LogoutView.as_view(),
        "name": "drf-logout",
    },
    {
        "route": "api/accounts/profile/",
        "view": ProfileView.as_view(),
        "name": "drf-profile",
    },
    {
        "route": "api/accounts/register/",
        "view": RegisterView.as_view(),
        "name": "drf-register",
    },
    {
        "route": "api/accounts/reset-password/",
        "view": ResetPasswordView.as_view(),
        "name": "drf-reset_password",
    },
    {
        "route": "api/accounts/reset-password/<uidb64>/<token>/",
        "view": ResetPasswordConfirmView.as_view(),
        "name": "drf-reset_password_confirm",
    },
    {
        "route": "api/accounts/reset-password/complete/",
        "view": ResetPasswordCompleteView.as_view(),
        "name": "drf-reset_password_complete",
    },
    {
        "route": "api/accounts/set-password/",
        "view": SetPasswordView.as_view(),
        "name": "drf-set_password",
    },
    {
        "route": "api/accounts/verify/",
        "view": VerifyView.as_view(),
        "name": "drf-verify",
    },
]

router = APIRouter(singleViews=singleViews)
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
    [path(route=i["route"], view=i["view"], name=i["name"]) for i in singleViews]
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
