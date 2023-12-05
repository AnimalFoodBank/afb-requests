import logging

from django.utils.module_loading import import_string as django_import_string
from rest_framework import serializers
from drf_registration.settings import drfr_settings
from drf_registration.utils.common import import_string

from drf_registration.utils.users import (
    get_user_profile_data,
    get_user_serializer,
    has_user_activate_token,
    has_user_verify_code,
    set_user_verified,
)

logger = logging.getLogger(__name__)


class RegisterSerializer(get_user_serializer()):
    """
    We completely override the default serializer to handle password validation.

    Due to some sensitive circular imports, we implement the logic from
    dsf_registration.api.register.RegisterSerializer here.
    """

    def validate_password(self, value):
        """
        Always pass password validation on registration. We do this
        b/c we want users to register without a password and then
        set a password later if needed. A case where it wouldn't be
        is allowing passwordless login via email.
        """
        # See no evil, speak no evil
        return value

    def create(self, validated_data):
        """
        Override create method to explicitly set an unusable password.
        """

        # Set an arbitrary value to the password field so that
        # the default create method doesn't throw an error.
        validated_data["password"] = "!"  # noqa: B105

        user = super().create(validated_data)

        # Sets the password field to have an arbitrary string
        # prefixed with "!" to indicate that the password is
        # unusable. This is a Django feature that allows us to
        # create users without a password. The user can login
        # via email link and set a password later.
        user.set_unusable_password()

        # Disable verified if enable verify user, else set it enabled
        user_verified = not (has_user_activate_token() or has_user_verify_code())
        set_user_verified(user, user_verified)

        user.save()
        return user
