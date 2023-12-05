"""
  URL configuration for non-Viewset views in DRF API.

  This is a list of dictionaries that can be passed to the APIRouter class
  in apps/api/contrib/api_router.py to add non-viewset views to the root
  page of the API. This is useful for adding views like Login, Logout, etc.

  NOTE: These views are not meant to be used in production. They are meant
  to be used for testing and development. They are not secure and should
  only be used when DEBUG.
"""

from afbcore.views import RegisterView
from drf_registration.api.change_password import ChangePasswordView
from drf_registration.api.login import LoginView, SocialLoginView
from drf_registration.api.logout import LogoutView
from drf_registration.api.profile import ProfileView
from drf_registration.api.register import ActivateView, VerifyView
from drf_registration.api.reset_password import (
    ResetPasswordCompleteView,
    ResetPasswordConfirmView,
    ResetPasswordView,
)
from drf_registration.api.set_password import SetPasswordView

EXTRA_API_VIEWS = [
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
