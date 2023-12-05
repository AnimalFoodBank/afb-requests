import logging

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from rest_framework import status as status_codes
from rest_framework.response import Response

from drf_registration.utils.users import (
    has_user_activate_token,
    has_user_verify_code,
    set_user_verified,
)

from drf_registration.api.register import (
    RegisterView as BaseRegistrationView,
    RegisterSerializer as BaseRegisterSerializer,
)
from drf_registration.settings import drfr_settings

logger = logging.getLogger(__name__)


class RegisterView(BaseRegistrationView):
    """
    Override the default registration view to handle exceptions.

    In terms of registering, all profile types are the same. The only

    """

    def create(self, request, *args, **kwargs):

        status, error_message = None, None
        email_address = request.data.get("email")

        try:
            # Attempt to create the user using the default
            # serializer from drf_registration.
            response = super().create(request, *args, **kwargs)

        # Handle db errors
        except IntegrityError as e:
            logger.warning(e)
            status = status_codes.HTTP_400_BAD_REQUEST
            error_message = "Unable to create user"

        # Handle issues sending mail via SMTP (e.g. Mailpit). Without this,
        # the user is created but the UI shows an error. We want to
        # continue with the request and we can try later to send the
        # email again.
        # NOTE: This is not a good idea for production. We should
        # use a task queue like Celery to handle this.
        except ConnectionRefusedError as e:
            logger.warning(f"Unable to send email to {email_address}: {e}")

        # This can also include "email already exists" errors
        except ValidationError as e:
            logger.error(e)
            status = status_codes.HTTP_400_BAD_REQUEST
            error_message = str(e)

        # Handle other exceptions gracefully
        except Exception as e:
            # Log the stack trace along with the error message
            # in case it helps debug the issue.
            logger.exception(e)
            logger.error(f"{e.__class__.__name__}: {e} ({email_address})")

            status = status_codes.HTTP_400_BAD_REQUEST
            error_message = str(e)

        # If we have an error, return a response with the error message.
        if status:
            response = Response({"error": error_message}, status=status)

        # Otherwise, return the response from the super class.
        return response
