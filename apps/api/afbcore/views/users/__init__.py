import logging

from django.contrib.auth import get_user_model
from rest_framework import permissions, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

from ...serializers import UserSerializer

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
    serializer_class = UserSerializer  # must be a class, not string

    # both permissions and authentication are required for
    # the viewset to be protected (and usable).
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    @action(detail=False, methods=["get"])
    def current_user(self, request, version=None, *args, **kwargs):
        """
        Retrieve the current authenticated user.
        """
        logger.debug("API Version: #{version}")
        serializer = self.get_serializer(request.user, context={"request": request})
        return Response(serializer.data)

    def get_queryset(self):
        """
        This view should return a list of all the users/profiles
        for the currently authenticated user.
        """
        if self.action == "list":
            return User.objects.none()  # disable list view
        return super().get_queryset()

    def destroy(self, request, *args, **kwargs):
        """
        Override destroy method to disable delete action
        """
        return Response(
            {"detail": "Delete action is disabled"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )
