import statistics
import os
import django
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


import pytest
from afbcore.views.users import UserViewSet
from rest_framework import status
from rest_framework.test import APITestCase

# python manage.py test afbcore.tests
# python manage.py test afbcore.tests.views.test_userview_register.RegisterTestCase


class RegisterTestCase(APITestCase):
    def setUp(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "afbcore.settings")
        User = get_user_model()
        self.client = APIClient()
        self.user = User.objects.create(
            username="testuser", email="testuser@test.com", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)

    # Register a new user with valid data
    def test_register_valid_data(self):
        # django.setup()

        # Initialize the UserViewSet object
        user_viewset = UserViewSet()

        # Create a valid data dictionary
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123",
        }

        # Call the register method with the valid data
        response = user_viewset.register(data)

        # Assert that the response status code is 201
        assert response.status_code == status.HTTP_201_CREATED

        # Assert that the response data matches the input data
        assert response.data == data

    # Register a new user with minimum required data
    def test_register_minimum_data(self):
        # Initialize the UserViewSet object
        user_viewset = UserViewSet()

        # Create a minimum required data dictionary
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123",
        }

        # Call the register method with the minimum required data
        response = user_viewset.register(data)

        # Assert that the response status code is 201
        assert response.status_code == status.HTTP_201_CREATED

        # Assert that the response data matches the input data
        assert response.data == data

    # Register a new user with all optional data
    def test_register_all_optional_data(self):
        # Initialize the UserViewSet object
        user_viewset = UserViewSet()

        # Create a data dictionary with all optional fields
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123",
            "is_staff": True,
        }

        # Call the register method with the data containing all optional fields
        response = user_viewset.register(data)

        # Assert that the response status code is 201
        assert response.status_code == status.HTTP_201_CREATED

        # Assert that the response data matches the input data
        assert response.data == data

    # Register a new user with an invalid email format
    def test_register_invalid_email_format(self):
        # Initialize the UserViewSet object
        user_viewset = UserViewSet()

        # Create a data dictionary with an invalid email format
        data = {
            "username": "testuser",
            "email": "invalid_email",
            "password": "password123",
        }

        # Call the register method with the data containing an invalid email format
        response = user_viewset.register(data)

        # Assert that the response status code is 400
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        # Assert that the response contains an error message for the email field
        assert "email" in response.data

    # Register a new user with an invalid username format
    def test_register_invalid_username_format(self):
        # Initialize the UserViewSet object
        user_viewset = UserViewSet()

        # Create a data dictionary with an invalid username format
        data = {
            "username": "invalid username",
            "email": "testuser@example.com",
            "password": "password123",
        }

        # Call the register method with the data containing an invalid username format
        response = user_viewset.register(data)

        # Assert that the response status code is 400
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        # Assert that the response contains an error message for the username field
        assert "username" in response.data

    # Register a new user with a password that is too short
    def test_register_short_password(self):
        # Initialize the UserViewSet object
        user_viewset = UserViewSet()

        # Create a data dictionary with a short password
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "pass",
        }

        # Call the register method with the data containing a short password
        response = user_viewset.register(data)

        # Assert that the response status code is 400
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        # Assert that the response contains an error message for the password field
        assert "password" in response.data
