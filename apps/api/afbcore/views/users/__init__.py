import logging

from django.contrib.auth import get_user_model
from drfpasswordless.utils import create_authentication_token
from rest_framework import permissions, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from ...serializers import UserSerializer

User = get_user_model()

logger = logging.getLogger(__name__)


# Example of a viewset with custom actions.
#
class CurrentUserAPIView(RetrieveAPIView):
    """
    API endpoint for the currently logged in user. No access to
    other users is made available through this endpoint.
    """

    # TODO: Use a more limited queryset. This makes all users available to all
    # usersto this endpoint. Can't spill beans you don't have.
    queryset = User.objects.none()
    serializer_class = UserSerializer  # must be a class, not string
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, version=None, *args, **kwargs):
        """
        Retrieve the current authenticated user.
        """
        logger.debug("API Version: #{version}")
        serializer = self.get_serializer(
            request.user, context={"request": request}
        )
        return Response(serializer.data)


class RegisterUserAPIView(CreateAPIView):
    throttle_scope = "signups"
    queryset = User.objects.none()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        data = serializer.data

        headers = self.get_success_headers(data)

        # Get or create token for user
        (token, _) = create_authentication_token(user=user)

        # Add the authentication token to the response. The Nuxt
        # UI will store this token in the browser's local storage
        # and use it to authenticate requests to the API.
        data["token"] = token.key

        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
