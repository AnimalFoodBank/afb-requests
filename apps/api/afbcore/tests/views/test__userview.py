"""
This module contains test cases for the UserViewSet API.

The UserViewSetTestCase class contains test cases for the following API endpoints:
- GET /users/
- POST /users/
- GET /users/{id}/
- PUT /users/{id}/
- DELETE /users/{id}/

To run the test cases, execute the following command:
python manage.py test afbcore.tests.views.test__userview.UserViewSetTestCase
"""

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse


class UserViewSetTestCase(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.client = APIClient()
        self.user = User.objects.create(
            username="testuser", email="testuser@test.com", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)

    def test_list_users(self):
        url = reverse("user-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        url = reverse("user-list")
        User = get_user_model()
        data = {
            "username": "newuser",
            "email": "newuser@test.com",
            "password": "newpassword",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.last().username, "newuser")

    def test_retrieve_user(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], self.user.username)

    def test_update_user(self):
        url = reverse("user-detail", args=[self.user.id])
        data = {
            "username": "updateduser",
            "email": "updateduser@test.com",
            "password": "updatedpassword",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, "updateduser")
        self.assertEqual(self.user.email, "updateduser@test.com")

    def test_delete_user(self):
        User = get_user_model()
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)
