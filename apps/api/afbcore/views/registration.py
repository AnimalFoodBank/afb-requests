import logging

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from rest_framework import status
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

        try:
            # Attempt to create

            response = super().create(request, *args, **kwargs)

        # Handle db errors
        except IntegrityError as e:
            logger.warning(e)
            response = Response(
                {"error": "Account with that email already exists."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Handle issues sending mail via SMTP (e.g. Mailpit). Without this,
        # the user is created but the UI shows an error. We want to
        # continue with the request and we can try later to send the
        # email again.
        # NOTE: This is not a good idea for production. We should
        # use a task queue like Celery to handle this.
        except ConnectionRefusedError as e:
            logger.warning(e)
            response = Response(
                {"error": "Unable to send mail."},
                status=status.HTTP_201_SERVICE_UNAVAILABLE,
            )

        # This can also include "email already exists" errors
        except ValidationError as e:
            logger.error(e)
            response = Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Handle other exceptions gracefully
        except Exception as e:
            logger.error(e)

            # Also log stack trace
            logger.exception(e)

            response = Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return response


# from rest_framework import generics
# from rest_framework.authtoken.models import Token
# from rest_framework.authtoken.serializers import AuthTokenSerializer

# from afbcore.models import User
# from afbcore.serializers import UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
