from afbcore.serializers import RegisterUserSerializer, UserSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from django.conf import settings
from datetime import datetime, timedelta

from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

User = get_user_model()


from rest_framework.authentication import TokenAuthentication, exceptions

# Example of a viewset with custom actions.
#
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    # TODO: Use a more limited queryset. This makes all users available to all
    # usersto this endpoint. Can't spill beans you don't have.
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["get"])
    def current_user(self, request):
        """
        Retrieve the current authenticated user.
        """
        serializer = self.get_serializer(request.user, context={"request": request})
        return Response(serializer.data)

    @api_view(["POST"])
    def register(request):
        """
        Register a new user.
        """
        serializer = UserSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["delete"])  # TODO: NOT WORKING
    def expire_token(self, request):
        model = TokenAuthentication.model

        try:
            token = model.objects.get(key=key)

        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed("Invalid token.")

        if self.expired(token):
            token.delete()
            raise exceptions.AuthenticationFailed("Token has expired.")

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed("User inactive or deleted.")

        return token.user, token

    @staticmethod
    def expired(token) -> bool:
        limit = settings.TOKEN_EXPIRED_AFTER
        now = datetime.now()
        return token.created < (now - timedelta(weeks=limit))
