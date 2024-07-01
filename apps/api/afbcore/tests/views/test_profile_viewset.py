# apps/api/afbcore/tests/views/test_profile_viewset.py

from afbcore.models import Pet, Profile
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

User = get_user_model()

"""
 How to run the tests:
     - pnpm django:test apps/api/afbcore/tests/views/test_profile_viewset.py
     - pytest apps/api/afbcore/tests/views/test_profile_viewset.py -v -k test_reconcile_pets_remove
"""


class ProfileViewSetTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            email="user1@test.com", name="name123"
        )
        self.user2 = User.objects.create_user(
            email="user2@test.com", name="name123"
        )
        # Create tokens for both users
        self.token1 = Token.objects.create(user=self.user1)
        self.token2 = Token.objects.create(user=self.user2)

        # Initially authenticate as user1
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token1.key)

        # Profiles are created automatically when a user is created.
        # See signals.py.
        self.profile1 = self.user1.get_default_profile()
        self.profile2 = self.user2.get_default_profile()

        # An extra profile for user2
        self.profile3 = Profile.objects.create(user=self.user2)

        self.pet1 = Pet.objects.create(
            pet_name="Pet1",
            profile=self.profile1,
            pet_type="dog",
            pet_dob="2020",
        )

        # Profile 1, user 1 is the default user for these tests
        # self.client.force_authenticate(user=self.user1)

        self.list_url = reverse("profile-list", kwargs={"version": "v1"})
        self.detail_url = reverse(
            "profile-detail", kwargs={"version": "v1", "pk": self.profile1.pk}
        )
        self.reconcile_url = reverse(
            "profile-reconcile-pets",
            kwargs={"version": "v1", "pk": self.profile1.pk},
        )

    def test_get_profile_list(self):
        response = self.client.get(self.list_url)
        count = response.data["count"]
        results = response.data["results"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(count, 1)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], str(self.profile1.id))

    def test_get_profile_list_as_user2(self):
        # Clear previous credentials and set new ones for user2
        self.client.credentials()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token2.key)
        response = self.client.get(self.list_url)

        # For debugging
        print(f"Authenticated user: {response.wsgi_request.user}")
        print(f"Response data: {response.data}")

        count = response.data["count"]
        results = response.data["results"]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(count, 2)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["id"], str(self.profile2.id))
        self.client.credentials()  # Clear credentials after the test

    def test_get_profile_list_multiple(self):
        response = self.client.get(self.list_url)
        count = response.data["count"]
        results = response.data["results"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(count, 1)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], str(self.profile1.id))

    def test_get_profile_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], str(self.profile1.id))

    def test_update_own_profile(self):
        data = {"preferred_name": "Updated Name"}
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.profile1.refresh_from_db()
        self.assertEqual(self.profile1.preferred_name, "Updated Name")

    def test_update_other_user_profile(self):
        other_profile_url = reverse(
            "profile-detail", kwargs={"version": "v1", "pk": self.profile2.pk}
        )
        data = {"preferred_name": "Updated Name"}
        response = self.client.patch(other_profile_url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_profile_not_allowed(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_reconcile_pets_add(self):
        data = {
            "pets": [
                {
                    "id": str(self.pet1.id),
                    "pet_name": "Updated Pet1",
                    "pet_type": "dog",
                    "pet_dob": "2020",
                },
                {"pet_name": "New Pet", "pet_type": "cat", "pet_dob": "2021"},
            ]
        }
        response = self.client.post(self.reconcile_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Pet.objects.count(), 2)
        self.assertTrue(Pet.objects.filter(pet_name="New Pet").exists())

    def test_reconcile_pets_update(self):
        data = {
            "pets": [
                {
                    "id": str(self.pet1.id),
                    "pet_name": "Updated Pet1",
                    "pet_type": "cat",
                    "pet_dob": "2019",
                }
            ]
        }
        response = self.client.post(self.reconcile_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.pet1.refresh_from_db()
        self.assertEqual(self.pet1.pet_name, "Updated Pet1")
        self.assertEqual(self.pet1.pet_type, "cat")
        self.assertEqual(self.pet1.pet_dob, "2019")

    def test_reconcile_pets_remove(self):
        Pet.objects.create(
            pet_name="Pet2",
            profile=self.profile1,
            pet_type="cat",
            pet_dob="2021",
        )
        data = {
            "pets": [
                {
                    "id": str(self.pet1.id),
                    "pet_name": "Pet1",
                    "pet_type": "dog",
                    "pet_dob": "2020",
                }
            ]
        }
        response = self.client.post(self.reconcile_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Pet.objects.count(), 1)
        self.assertFalse(Pet.objects.filter(pet_name="Pet2").exists())

    def test_reconcile_pets_invalid_data(self):
        data = {"pets": "not a list"}
        response = self.client.post(self.reconcile_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_reconcile_pets_nonexistent_pet(self):
        data = {
            "pets": [
                {
                    "id": "614d1ca1-a0bc-4694-a2ec-6ac3b433802e",  # "nonexistent-id",
                    "pet_name": "Nonexistent Pet",
                    "pet_type": "dog",
                    "pet_dob": "2020",
                }
            ]
        }
        response = self.client.post(self.reconcile_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unauthenticated_access(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_access_different_user(self):
        self.client.force_authenticate(user=self.user1)
        reconcile_url2 = reverse(
            "profile-reconcile-pets",
            kwargs={
                "version": "v1",
                "pk": self.profile2.pk,
            },  # user 2's profile
        )

        response = self.client.get(reconcile_url2)
        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED
        )
