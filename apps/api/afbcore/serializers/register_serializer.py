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
        validated_data["password"] = "!unusable"  # noqa B105

        response = super().create(validated_data)
        # user.set_unusable_password()

        return response
