#
# Github Copilot
#

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIFoodRequestFactory
from rest_framework.test import force_authenticate
from afbcore.views import FoodFoodRequestViewSet
from afbcore.models import FoodFoodRequest
from afbcore.serializers import FoodRequestSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class FoodFoodRequestViewSetTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email="testuser@example.com", password="testpassword"
        )
        cls.food_request = FoodFoodRequest.objects.create(
            title="Test FoodRequest", description="Test Description", user=cls.user
        )

    def setUp(self):
        self.factory = APIFoodRequestFactory()
        self.view = FoodFoodRequestViewSet.as_view(
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
        data = {"title": "New FoodRequest", "description": "New Description"}
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
        data = {"title": "Updated FoodRequest", "description": "Updated Description"}
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
