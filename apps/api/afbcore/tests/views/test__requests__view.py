#
# Github Copilot
#

from afbcore.models import FoodRequest
from afbcore.serializers import FoodRequestCreateSerializer
from afbcore.views import FoodRequestViewSet
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

User = get_user_model()


class FoodRequestViewSetTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email="testuser@example.com", password="testpassword"
        )
        cls.food_request = FoodRequest.objects.create(
            user=cls.user,
        )

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = FoodRequestViewSet.as_view(
            {
                "get": "list",
                "post": "create",
                "put": "update",
                "patch": "partial_update",
            }
        )
        self.url = "/requests/"
