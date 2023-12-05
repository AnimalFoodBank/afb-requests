import os
import uuid

from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APITestCase
from afbcore.views.users import UserViewSet, RegisterView
from afbcore.serializers import UserSerializer, RegisterSerializer
from django.test import RequestFactory

"""
How to run the tests:
    - python manage.py test apps/api/afbcore/tests/views/test_users.py
    - python manage.py test afbcore.tests.views.test_users.RegisterTestCase.test_register_valid_data


"""

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "afbcore.settings")


class RegisterViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        unique_username = "testuser" + str(uuid.uuid4())
        cls.user = User.objects.create(
            username=unique_username,
            email=unique_username + "@example.com",
            password="testpassword",
        )

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def tearDown(self):
        User = get_user_model()
        User.objects.all().delete()

    # Register a new user with valid data
    def test_register_valid_data(self):
        # Create a valid data dictionary
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123",
        }

        # Create a mock request
        factory = RequestFactory()
        request = factory.post("/users/", data, format="json")

        # Create a RegisterSerializer instance with the valid data
        serializer = RegisterSerializer(data=data, context={"request": request})

        if not serializer.is_valid():
            # Output the serializer errors when it's not valid
            print(serializer.errors)

        # Check if the serializer is valid
        self.assertTrue(serializer.is_valid())

        # Call the post method of RegisterView with the valid data
        view = RegisterView.as_view()
        response = view(request)

        # Assert that the response status code is 201
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the response data matches the input data
        self.assertEqual(response.data, serializer.data)

    # Register a new user with minimum required data
    def test_register_minimum_data(self):
        # Create a minimum required data dictionary
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123",
        }

        # Create a RegisterSerializer instance with the minimum required data
        serializer = RegisterSerializer(data=data)

        # Check if the serializer is valid
        serializer.is_valid()

        # Call the post method of RegisterView with the minimum required data
        factory = RequestFactory()
        request = factory.post("/users/", data, format="json")
        view = RegisterView.as_view()
        response = view(request)

        # Assert that the response status code is 201
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the response data matches the input data
        self.assertEqual(response.data, serializer.data)

    # Register a new user with all optional data
    def test_register_all_optional_data(self):
        # Create a data dictionary with all optional fields
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123",
            "is_staff": True,
        }

        # Initialize the RegisterSerializer object with the data containing all optional fields
        serializer = RegisterSerializer(data=data)

        # Check if the serializer is valid
        if serializer.is_valid():
            # Call the post method of RegisterView with the data containing all optional fields
            factory = RequestFactory()
            request = factory.post("/users/", data, format="json")
            view = RegisterView.as_view()
            response = view(request)

            # Assert that the response status code is 201
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            # Assert that the response data matches the input data
            self.assertEqual(response.data, serializer.data)
        else:
            # If the serializer is not valid, raise an AssertionError
            raise AssertionError(serializer.errors)

        # Assert that the response data matches the input data
        self.assertEqual(response.data, data)

    # Register a new user with an invalid email format
    def test_register_invalid_email_format(self):
        # Create a data dictionary with an invalid email format
        data = {
            "username": "testuser",
            "email": "invalid_email",
            "password": "password123",
        }

        # Initialize the RegisterSerializer object with the data containing an invalid email format
        serializer = RegisterSerializer(data=data)

        # Check if the serializer is valid
        if serializer.is_valid():
            # Call the post method of RegisterView with the valid data
            factory = RequestFactory()
            request = factory.post("/users/", data, format="json")
            view = RegisterView.as_view()
            response = view(request)

            # Assert that the response status code is 400
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

            # Assert that the response contains an error message for the email field
            self.assertIn("email", response.data)
        else:
            # Assert that the serializer is invalid
            self.fail("Serializer is invalid")

    # Register a new user with an invalid username format
    def test_register_invalid_username_format(self):
        # Create a data dictionary with an invalid username format
        data = {
            "username": "invalid username",
            "email": "testuser@example.com",
            "password": "password123",
        }

        # Initialize the RegisterSerializer object with the data containing an invalid username format
        serializer = RegisterSerializer(data=data)

        # Check if the serializer is valid
        if serializer.is_valid():
            # Call the post method of RegisterView with the valid data
            factory = RequestFactory()
            request = factory.post("/users/", data, format="json")
            view = RegisterView.as_view()
            response = view(request)

            # Assert that the response status code is 400
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

            # Assert that the response contains an error message for the username field
            self.assertIn("username", response.data)
        else:
            # If the serializer is not valid, raise an AssertionError with the serializer errors
            raise AssertionError(serializer.errors)

    # Register a new user with a password that is too short
    def test_register_short_password(self):
        # Create a data dictionary with a short password
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "pass",
        }

        # Initialize the RegisterSerializer object with the data containing a short password
        serializer = RegisterSerializer(data=data)

        # Check if the serializer is valid
        if serializer.is_valid():
            # Call the post method of RegisterView with the valid data
            factory = RequestFactory()
            request = factory.post("/users/", data, format="json")
            view = RegisterView.as_view()
            response = view(request)

            # Assert that the response status code is 400
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

            # Assert that the response contains an error message for the password field
            self.assertIn("password", response.data)
        else:
            # If the serializer is not valid, raise an AssertionError
            raise AssertionError("Serializer is not valid")
