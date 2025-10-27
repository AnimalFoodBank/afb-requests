from afbcore.models import FoodRequest
from afbcore.serializers import (
    FoodRequestCreateSerializer,
    FoodRequestUpdateSerializer,
)
from afbcore.views.food_request_view import FoodRequestViewSet
from django.test import RequestFactory
from rest_framework.test import APIRequestFactory, APITestCase


class FoodRequestViewSetAPITestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = FoodRequestViewSet()

    def test_get_serializer_class_post(self):
        request = self.factory.post("/food-requests/")
        self.view.request = request
        serializer_class = self.view.get_serializer_class()
        self.assertEqual(serializer_class, FoodRequestCreateSerializer)

    def test_get_serializer_class_other_methods(self):
        request = self.factory.get("/food-requests/")
        self.view.request = request
        serializer_class = self.view.get_serializer_class()
        self.assertEqual(serializer_class, FoodRequestUpdateSerializer)
