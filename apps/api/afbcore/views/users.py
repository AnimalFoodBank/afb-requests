# trunk-ignore-all(isort)
import logging
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from rest_framework import generics, permissions, status, viewsets
from rest_framework.authentication import TokenAuthentication, exceptions
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


User = get_user_model()

logger = logging.getLogger(__name__)


# Example of a viewset with custom actions.
#
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    # TODO: Use a more limited queryset. This makes all users available to all
    # usersto this endpoint. Can't spill beans you don't have.
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = "afbcore.serializers.user_serializer.UserSerializer"
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["get"])
    def current_user(self, request):
        """
        Retrieve the current authenticated user.
        """
        serializer = self.get_serializer(request.user, context={"request": request})
        return Response(serializer.data)

    @action(detail=False, methods=["delete"])
    def expire_token(self, request):
        model = Token

        # e.g. "Token 9944b09..."
        header_str = request.META.get("HTTP_AUTHORIZATION", "")

        # Splitting the string into two parts, The literal "Token"
        # prefix and the key itself. The default is an empty
        # string so this will always return a list of at
        # least one item.
        _, *key = header_str.split(" ")

        # We use the asterisk to unpack the list into two variables
        # where the second variable is a list of all the remaining
        # items in the list. If there is no authorization key, the
        # list will be empty. If there is an authorization key, we
        # reassign `key` with the first item in the list (to make
        # it a string again).
        if key:
            key = key.get(0)

        # Get the token from the request header.
        if key is None:
            logger.warning("Token is none. Token: %s", key)
            raise exceptions.AuthenticationFailed("Invalid token (1).")

        try:
            token = model.objects.get(key=key, user=request.user)

        except model.DoesNotExist:
            logger.warning("Token does not exist. Token: %s", key)
            raise exceptions.AuthenticationFailed("Invalid token (2).")

        if self.expired(token):
            token.delete()
            logger.warning("Token has expired for user: %s", request.user)
            raise exceptions.AuthenticationFailed("Token has expired.")

        if not token.user.is_active:
            logger.warning("User is inactive: %s", token.user)
            raise exceptions.AuthenticationFailed("User inactive or deleted.")

        return token.user, token

    @staticmethod
    def expired(token) -> bool:
        limit = settings.TOKEN_EXPIRED_AFTER
        now = datetime.now()
        return token.created < (now - timedelta(weeks=limit))
