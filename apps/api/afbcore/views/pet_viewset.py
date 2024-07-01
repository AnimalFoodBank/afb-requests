# apps/api/afbcore/views/pet_viewset.py

import logging

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied, ValidationError

from ..models import Pet
from ..serializers import PetSerializer
from .base import UserFilterBaseViewSet

logger = logging.getLogger(__name__)


class PetViewSet(UserFilterBaseViewSet):
    """
    API endpoint for Pet CRUD operations, limited to Pets
    associated with the currently logged in user's profiles.
    """

    queryset = Pet.objects.order_by("-created")
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        """
        This view should return a list of all pets
        for the currently authenticated user's profiles.
        """
        user = self.request.user
        return Pet.objects.filter(profile__user=user).order_by("-created")

    def perform_create(self, serializer):
        """
        When creating a new pet, associate it with one of the user's profiles.
        """
        user = self.request.user
        try:
            # Get the first profile of the user
            profile = user.profiles.first()
            if profile is None:
                raise ObjectDoesNotExist
            serializer.save(profile=profile)
        except ObjectDoesNotExist:
            raise ValidationError(
                "User does not have any profiles. Please create a profile first."
            )

    def perform_update(self, serializer):
        """
        Ensure that the user can only update pets associated with their profiles.
        """
        instance = self.get_object()
        user = self.request.user

        try:
            # Check if the pet's profile belongs to the user
            user.profiles.get(id=instance.profile.id)
            serializer.save()
        except ObjectDoesNotExist:
            raise PermissionDenied(
                "You can only update pets associated with your profiles."
            )

    def perform_destroy(self, instance):
        """
        Ensure that the user can only delete pets associated with their profiles.
        """
        user = self.request.user

        try:
            # Check if the pet's profile belongs to the user
            user.profiles.get(id=instance.profile.id)
            instance.delete()
        except ObjectDoesNotExist:
            raise PermissionDenied(
                "You can only delete pets associated with your profiles."
            )
