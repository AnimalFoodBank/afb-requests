from unittest import skip
from django.contrib.auth import get_user_model
from django.test import TestCase as DjangoTestCase
from django.core.exceptions import ValidationError

"""
    Run these tests with the following command:
    python manage.py test afbcore.tests.models.test_user
    python manage.py test afbcore/tests/models --pattern="test_user.py"
"""


class TestCase(DjangoTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.User = get_user_model()

    def test_create_user(self):
        user = self.User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123",
            first_name="Test",
            last_name="User",
        )

        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")
        self.assertTrue(user.check_password("password123"))

    def test_create_superuser(self):
        superuser = self.User.objects.create_superuser(
            username="testsuperuser",
            email="testsuperuser@example.com",
            password="password123",
            first_name="Test",
            last_name="Superuser",
        )

        self.assertEqual(superuser.username, "testsuperuser")
        self.assertEqual(superuser.email, "testsuperuser@example.com")
        self.assertEqual(superuser.first_name, "Test")
        self.assertEqual(superuser.last_name, "Superuser")
        self.assertTrue(superuser.check_password("password123"))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_delete_user(self):
        user = self.User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123",
            first_name="Test",
            last_name="User",
        )

        user.delete()

        self.assertFalse(self.User.objects.filter(username="testuser").exists())

    def test_delete_superuser(self):
        superuser = self.User.objects.create_superuser(
            username="testsuperuser",
            email="testsuperuser@example.com",
            password="password123",
            first_name="Test",
            last_name="Superuser",
        )

        superuser.delete()

        self.assertFalse(self.User.objects.filter(username="testsuperuser").exists())

    # Can change a regular user's password
    def test_user_password_change(self):
        user = self.User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123",
            first_name="Test",
            last_name="User",
        )

        user.set_password("newpassword123")
        user.save()

        self.assertTrue(user.check_password("newpassword123"))

    # Can create a user without a password
    def test_create_user_without_password(self):
        user = self.User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            first_name="Test",
            last_name="User",
        )

        self.assertFalse(user.has_usable_password())

    # Email address too long
    @skip("This test is being skipped")
    def test_create_user_with_long_email(self):
        with self.assertRaises(ValidationError):
            self.User.objects.create_user(
                username="testuser",
                email="a" * 2550 + "@example.com",
                password="password123",
                first_name="Test",
                last_name="User",
            )
