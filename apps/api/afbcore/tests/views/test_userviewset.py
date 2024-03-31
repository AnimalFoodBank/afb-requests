from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from afbcore.views import UserViewSet
from afbcore.models import Request
from afbcore.serializers import RequestSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UsersViewSetTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email="testuser@example.com", password="testpassword"
        )
        cls.request = Request.objects.create(
            title="Test Request", description="Test Description", user=cls.user
        )

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = UserViewSet.as_view(
            {
                "get": "list",
                "post": "create",
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
            }
        )
        self.url = "/requests/"

    # Returns a response with status code 405 and a message "Delete action is disabled".
    def test_returns_response_with_status_code_405_and_message(self):
        # Initialize the UserViewSet object
        viewset = UserViewSet()

        # Invoke the destroy method
        response = viewset.destroy(None)

        # Check the response status code and message
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert response.data == {"detail": "Delete action is disabled"}

    # Returns a response with status code 200 and the correct serialized data
    def test_returns_response_with_status_code_200_and_correct_data(self):
        # Create a request object
        request = Request.objects.create(
            title="Test Request", description="Test Description", user=self.user
        )

        # Initialize the RequestViewSet object
        viewset = RequestViewSet()

        # Invoke the retrieve method
        response = viewset.retrieve(None, pk=request.id)

        # Check the response status code and data
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            "id": str(request.id),
            "title": "Test Request",
            "description": "Test Description",
            "user": str(self.user.id),
        }
