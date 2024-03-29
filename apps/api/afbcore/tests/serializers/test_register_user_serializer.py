from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from afbcore.serializers.register_user_serializer import RegisterUserSerializer

"""
    To run this test, run the following command:
    python manage.py test afbcore.tests.serializers.test_register_user_serializer
"""


class TestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.User = get_user_model()
        cls.valid_password = "xyz9.helloPLEASE"

    def test_register_user_serializer_valid_data(self):
        password_str = TestCase.valid_password
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": password_str,
            "password2": password_str,
            "first_name": "Test",
            "last_name": "User",
        }

        serializer = RegisterUserSerializer(data=data)
        is_valid = serializer.is_valid()

        if not is_valid:
            print(serializer.errors)

        self.assertNotIn("email", serializer.errors)
        self.assertNotIn("username", serializer.errors)
        self.assertNotIn("password", serializer.errors)
        self.assertNotIn("password2", serializer.errors)
        self.assertTrue(is_valid)

        user = serializer.save()
        self.assertEqual(user.username, data["username"])
        self.assertEqual(user.email, data["email"])
        self.assertEqual(user.first_name, data["first_name"])
        self.assertEqual(user.last_name, data["last_name"])

    def test_register_user_serializer_simple_password(self):
        # python manage.py test afbcore.tests.serializers.test_register_user_serializer.TestCase.test_register_user_serializer_simple_password
        password_str = "password123"
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": password_str,
            "password2": password_str,
            "first_name": "Test",
            "last_name": "User",
        }

        serializer = RegisterUserSerializer(data=data)
        is_valid = serializer.is_valid()

        if not is_valid:
            print(serializer.errors)

        self.assertNotIn("email", serializer.errors)
        self.assertNotIn("username", serializer.errors)
        self.assertIn("password", serializer.errors)
        self.assertNotIn("password2", serializer.errors)
        self.assertFalse(is_valid)

    def test_register_user_serializer_invalid_email(self):
        password_str = TestCase.valid_password
        data = {
            "username": "testuser",
            "email": "invalid_email",
            "password": password_str,
            "password2": password_str,
            "first_name": "Test",
            "last_name": "User",
        }

        serializer = RegisterUserSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)

    def test_register_user_serializer_password_mismatch(self):
        password_str = TestCase.valid_password
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": password_str,
            "password2": "password456",
            "first_name": "Test",
            "last_name": "User",
        }

        serializer = RegisterUserSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)

    def test_register_user_serializer_short_password(self):
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "fail",
            "password2": "fail",
            "first_name": "Test",
            "last_name": "User",
        }

        serializer = RegisterUserSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)
