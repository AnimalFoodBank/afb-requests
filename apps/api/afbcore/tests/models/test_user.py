from unittest import skip

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase as DjangoTestCase

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
            email="testuser@example.com",
            password="password123",
            name="User",
        )

        self.assertEqual(user.email, "testuser@example.com")
        self.assertEqual(user.name, "User")
        self.assertTrue(user.check_password("password123"))

    def test_create_superuser(self):
        superuser = self.User.objects.create_superuser(
            email="testsuperuser@example.com",
            password="password123",
            name="Superuser",
        )

        self.assertEqual(superuser.email, "testsuperuser@example.com")
        self.assertEqual(superuser.name, "Superuser")
        self.assertTrue(superuser.check_password("password123"))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_delete_user(self):
        user = self.User.objects.create_user(
            email="testuser@example.com",
            password="password123",
            name="User",
        )

        user.delete()

        self.assertFalse(
            self.User.objects.filter(email="testuser@example.com").exists()
        )

    def test_delete_superuser(self):
        superuser = self.User.objects.create_superuser(
            email="testsuperuser@example.com",
            password="password123",
            name="Superuser",
        )

        superuser.delete()

        self.assertFalse(
            self.User.objects.filter(email="testsuperuser@example.com").exists()
        )

    # Can change a regular user's password
    def test_user_password_change(self):
        user = self.User.objects.create_user(
            email="testuser@example.com",
            password="password123",
            name="User",
        )

        user.set_password("newpassword123")
        user.save()

        self.assertTrue(user.check_password("newpassword123"))

    # Can create a user without a password
    def test_create_user_without_password(self):
        user = self.User.objects.create_user(
            email="testuser@example.com",
            name="User",
        )

        self.assertFalse(user.has_usable_password())

    # Email address too long
    @skip("This test is being skipped")
    def test_create_user_with_long_email(self):
        with self.assertRaises(ValidationError):
            self.User.objects.create_user(
                email="a" * 2550 + "@example.com",
                password="password123",
                name="User",
            )


class UserManagerTestCase(DjangoTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.User = get_user_model()

    def test_is_a_truly_unique(self):
        user = self.User.objects.create_user(
            email="testuser@example.com",
            name="Test",
            password="password123",
        )

        manager = self.User.objects
        field_name = "email"
        value = "testuser@example.com"

        result = manager.is_a_truly_unique(field_name, value)
        self.assertFalse(result)

        value = "nonexistentuser"
        result = manager.is_a_truly_unique(field_name, value)
        self.assertTrue(result)
