import logging

from django.contrib.auth import get_user_model
from rest_framework import permissions, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from ...models import Profile
from ...serializers import ProfileSerializer
from ..base import UserFilterBaseViewSet

User = get_user_model()

logger = logging.getLogger(__name__)


# Example of a viewset with custom actions.
#
class ProfileViewSet(UserFilterBaseViewSet):
    """
    API endpoint for the Profile CRUD operations, limited to Profiles
    associated with the currently logged in user.
    """

    queryset = Profile.objects.order_by("-created_at")
    serializer_class = ProfileSerializer  # must be a class, not string
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    authentication_classes = [TokenAuthentication]

    # def get(self, request, version=None, *args, **kwargs):
    #     """
    #     Retrieve the current authenticated user.
    #     """
    #     logger.debug("API Version: #{version}")
    #     serializer = self.get_serializer(
    #         request.user, context={"request": request}
    #     )
    #     return Response(serializer.data)
