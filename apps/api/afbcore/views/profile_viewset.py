import logging

from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import permissions, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response

from ..models import Pet, Profile
from ..permissions import IsOwner
from ..serializers import PetSerializer, ProfileSerializer
from .base import UserFilterBaseViewSet

User = get_user_model()

logger = logging.getLogger(__name__)


"""

    The ProfileViewSet class is a viewset that provides CRUD operations
    for the Profile model and is limited to profile(s) associated with
    the currently logged in user. Even though multiple profiles can be
    associated with a user, currently the application only supports one
    profile per user (as of summer 2024).

    About permissions:
        The ProfileViewSet uses the IsOwner permission class to limit
        access to the profile(s) associated with the currently logged
        in user.

    About updating pets:
        The reconcile_pets method allows for adding, updating, and
        removing pets in a single operation, which is useful for
        synchronizing pet data with a client application.

        Example data in a POST request::
        {
            "pets": [
                {"id": "existing-pet-id", "pet_name": "Updated Name", "pet_type": "dog", "pet_dob": "2020-01-01"},
                {"pet_name": "New Pet", "pet_type": "Cat", "pet_dob": "2021-05-15"}
            ]
        }

"""


class ProfileViewSet(UserFilterBaseViewSet):
    """
    API endpoint for the Profile CRUD operations, limited to Profiles
    associated with the currently logged in user.
    """

    queryset = Profile.objects.order_by("-created")
    serializer_class = ProfileSerializer  # must be a class, not string
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwner,
    ]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        """
        Limit the available profiles to ones associated with the
        currently authenticated user.
        """
        return Profile.objects.filter(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed("DELETE")

    @action(detail=True, methods=["post"])
    @transaction.atomic
    def reconcile_pets(self, request, pk=None, version=None):
        """
        Reconcile the pets for a specific profile.

        Allows for adding, updating, and removing pets in a single
        operation. This method will:

        1. Add new pets that don't exist
        2. Update existing pets
        3. Remove pets that are not in the provided list

        It processes each pet in the list:
            - If the pet has an ID, it updates the existing pet.
            - If the pet doesn't have an ID, it creates a new pet.
            - Removes any pets that were associated with the profile
              but not included in the request data.

        Uses @transaction.atomic to ensure that all database operations
        are performed in a single transaction. e.g. the changes are
        either all saved or all rolled back in case of an error.

        """
        profile = self.get_object()
        pets_data = request.data.get("pets", [])

        if not isinstance(pets_data, list):
            return Response(
                {"error": "Pets data must be a list"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Create a set of existing pet IDs for this profile
        existing_pet_ids = set(
            str(id) for id in profile.pets.values_list("id", flat=True)
        )

        # Process each pet in the request
        processed_pet_ids = set()
        for pet_data in pets_data:
            pet_id = pet_data.get("id")

            if pet_id:
                # Update existing pet
                try:
                    pet = profile.pets.get(id=pet_id)
                    serializer = PetSerializer(pet, data=pet_data, partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    processed_pet_ids.add(str(pet_id))
                except Pet.DoesNotExist:
                    return Response(
                        {
                            "error": f"Pet with id {pet_id} does not exist for this profile"
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                # Create new pet
                serializer = PetSerializer(data=pet_data)
                serializer.is_valid(raise_exception=True)
                pet = serializer.save(profile=profile)
                processed_pet_ids.add(str(pet.id))

        # Remove pets that were not in the request
        pets_to_remove = existing_pet_ids - processed_pet_ids
        profile.pets.filter(id__in=pets_to_remove).delete()

        # Return updated profile with reconciled pets
        serializer = self.get_serializer(profile)
        return Response(serializer.data)
