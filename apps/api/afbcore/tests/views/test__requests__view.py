#
# Github Copilot
#

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from afbcore.views import RequestViewSet
from afbcore.models import FoodRequest
from afbcore.serializers import RequestSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class RequestViewSetTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email="testuser@example.com", password="testpassword"
        )
        cls.food_request = FoodRequest.objects.create(
            title="Test Request", description="Test Description", user=cls.user
        )

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = RequestViewSet.as_view(
            {
                "get": "list",
                "post": "create",
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
            }
        )
        self.url = "/requests/"

    def test_list_requests(self):
        request = self.factory.get(self.url)
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_request(self):
        data = {"title": "New Request", "description": "New Description"}
        request = self.factory.post(self.url, data)
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_request(self):
        request = self.factory.get(f"{self.url}{self.food_request.id}/")
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=self.food_request.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_request(self):
        data = {"title": "Updated Request", "description": "Updated Description"}
        request = self.factory.put(f"{self.url}{self.food_request.id}/", data)
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=self.food_request.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_request(self):
        data = {"description": "Updated Description"}
        request = self.factory.patch(f"{self.url}{self.food_request.id}/", data)
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=self.food_request.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_request(self):
        request = self.factory.delete(f"{self.url}{self.food_request.id}/")
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=self.food_request.id)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
