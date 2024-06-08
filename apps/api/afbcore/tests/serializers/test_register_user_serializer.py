from afbcore.serializers import UserSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.test import APITestCase

"""
    To run this test, run the following command:
    python manage.py test afbcore.tests.serializers.test_user_serializer
"""


class TestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.User = get_user_model()
        cls.valid_password = "xyz9.helloPLEASE"

    def test_user_serializer_valid_data(self):
        password_str = TestCase.valid_password
        data = {
            "name": "testuser",
            "email": "testuser@example.com",
        }

        serializer = UserSerializer(data=data)
        is_valid = serializer.is_valid()

        if not is_valid:
            print(serializer.errors)

        self.assertNotIn("email", serializer.errors)
        self.assertNotIn("name", serializer.errors)
        self.assertNotIn("password", serializer.errors)
        self.assertNotIn("password2", serializer.errors)
        self.assertTrue(is_valid)

        user = serializer.save()
        self.assertEqual(user.name, data["name"])
        self.assertEqual(user.email, data["email"])

    def test_user_serializer_invalid_email(self):
        data = {
            "name": "testuser",
            "email": "invalid_email",
        }

        serializer = UserSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)

    def test_user_serializer_password_ignored(self):
        password_str = TestCase.valid_password
        data = {
            "name": "testuser",
            "email": "testuser@example.com",
            "password": password_str,
            "password2": "password456",
        }

        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()

        # The given passwork doesn't match the literal value of
        # the field and doesn't match the hashed value either.
        self.assertFalse(user.password is None)
        self.assertNotEqual(user.password, password_str)
        self.assertFalse(check_password(password_str, user.password))

        self.assertTrue(len(serializer.errors) == 0)
