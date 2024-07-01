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
