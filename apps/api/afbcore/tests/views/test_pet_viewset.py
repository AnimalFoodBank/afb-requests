from afbcore.models.pet import Pet
from afbcore.models.users.profile import Profile
from afbcore.serializers import PetSerializer
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

User = get_user_model()


class PetViewSetTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email="user1", name="name1")
        self.user2 = User.objects.create_user(email="user2", name="name2")
        self.profile1 = Profile.objects.create(user=self.user1)
        self.profile2 = Profile.objects.create(user=self.user2)
        self.pet1 = Pet.objects.create(pet_name="Pet1", profile=self.profile1)
        self.pet2 = Pet.objects.create(pet_name="Pet2", profile=self.profile2)

        # The default client used in these tests is authenticated as user1
        self.token1 = Token.objects.create(user=self.user1)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token1.key)

        self.list_url = reverse("pet-list", kwargs={"version": "v1"})
        self.detail_url = reverse(
            "pet-detail", kwargs={"version": "v1", "pk": self.pet1.pk}
        )

    def tearDown(self):
        self.pet1.delete()
        self.pet2.delete()
        self.profile1.delete()
        self.profile2.delete()
        self.user1.delete()
        self.user2.delete()

    def test_get_pet_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["pet_name"], "Pet1")

    def test_get_pet_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["pet_name"], "Pet1")

    def test_create_pet(self):
        data = {
            "pet_name": "NewPet",
            "pet_type": "dog",
            "pet_dob": "2020",
        }
        response = self.client.post(self.list_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pet.objects.count(), 3)
        self.assertEqual(
            Pet.objects.get(pet_name="NewPet").profile, self.profile1
        )

    def test_update_own_pet(self):
        data = {
            "pet_name": "UpdatedPet",
            "pet_type": "dog",
            "pet_dob": "2020",
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.pet1.refresh_from_db()
        self.assertEqual(self.pet1.pet_name, "UpdatedPet")

    def test_update_other_user_pet(self):
        data = {"pet_name": "UpdatedPet"}
        other_pet_url = reverse(
            "pet-detail", kwargs={"version": "v1", "pk": self.pet2.pk}
        )
        response = self.client.put(other_pet_url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_own_pet(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Pet.objects.count(), 1)

    def test_delete_other_user_pet(self):
        other_pet_url = reverse(
            "pet-detail", kwargs={"version": "v1", "pk": self.pet2.pk}
        )
        response = self.client.delete(other_pet_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Pet.objects.count(), 2)

    def test_unauthenticated_access(self):
        self.client.credentials()  # Remove authentication
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_pet_missing_fields(self):
        data = {
            "pet_name": "NewPet",
            "pet_type": "dog",
            # Missing pet_dob field
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_pet_food_details(self):
        data = {"food_details": {"type": "dry", "brand": "Acme"}}
        response = self.client.patch(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.pet1.refresh_from_db()
        self.assertEqual(
            self.pet1.food_details, {"type": "dry", "brand": "Acme"}
        )

    def test_user_with_multiple_profiles(self):
        """Checks if a user can create and view pets across multiple profiles."""

        # Create a second profile for user1
        second_profile = Profile.objects.create(user=self.user1)

        # Create a pet for the second profile
        data = {
            "pet_name": "SecondProfilePet",
            "pet_type": "cat",
            "pet_dob": "2019",
            "profile": second_profile.id,
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check that the pet was created and associated with the correct profile
        created_pet = Pet.objects.get(pet_name="SecondProfilePet")
        self.assertEqual(created_pet.profile, second_profile)

        # Check that the user can see both pets in the list
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

    def test_create_pet_for_other_user_profile(self):
        """Ensures a user can't create a pet for a profile that doesn't belong to them."""
        data = {
            "pet_name": "OtherUserPet",
            "pet_type": "bird",
            "pet_dob": "2021",
            "profile": self.profile2.id,  # This profile belongs to user2
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_pet_to_different_profile_same_user(self):
        """Verifies that a user can move a pet between their own profiles."""
        # Create a second profile for user1
        second_profile = Profile.objects.create(user=self.user1)

        data = {"pet_name": "UpdatedPet", "profile": second_profile.id}
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.pet1.refresh_from_db()
        self.assertEqual(self.pet1.profile, second_profile)

    def test_update_pet_to_different_user_profile(self):  # fail
        """Checks that a user can't move a pet to a profile belonging to another user."""
        data = {
            "pet_name": "UpdatedPet",
            "profile": self.profile2.id,  # This profile belongs to user2
        }
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_pets_from_all_profiles(self):
        """Ensures that when listing pets, the user sees pets from all their profiles."""
        # Create a second profile for user1 and add a pet to it
        second_profile = Profile.objects.create(user=self.user1)
        Pet.objects.create(
            pet_name="SecondProfilePet",
            profile=second_profile,
            pet_type="cat",
            pet_dob="2019",
        )

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(response.data["results"]), 2
        )  # Should see pets from both profiles
