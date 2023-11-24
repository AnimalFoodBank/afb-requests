import logging

from drf_registration.utils.users import (
    has_user_activate_token,
    has_user_verify_code,
    set_user_verified,
)

from drf_registration.api.register import (
    RegisterSerializer as BaseRegisterSerializer,
)
from drf_registration.settings import drfr_settings

logger = logging.getLogger(__name__)


class RegisterSerializer(BaseRegisterSerializer):
    """
    We override the default serializer to handle password validation.
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
        user.save()

        return user
