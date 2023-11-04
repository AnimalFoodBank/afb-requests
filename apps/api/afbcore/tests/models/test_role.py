from django.test import TestCase
from afbcore.models.users.role import Role
from django.db.utils import IntegrityError

"""
    Run these tests with the following command:
    python manage.py test afbcore.tests.models.test_role
"""


class RoleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods

        cls.role = Role.objects.create(name="Test Role", level=90)

    def test_role_name_max_length(self):
        role = Role.objects.get(id=self.role.id)
        max_length = role._meta.get_field("name").max_length
        self.assertEqual(max_length, 50)

    def test_role_level_default_value(self):
        role = Role.objects.get(id=self.role.id)
        self.assertEqual(role.level, 90)

    def test_role_str_method(self):
        role = Role.objects.get(id=self.role.id)
        self.assertEqual(str(role), "Test Role")

    def test_role_name_required(self):
        with self.assertRaises(ValueError):
            Role.objects.create(level=1)

    def test_role_level_range(self):
        Role.objects.create(name="Test Role 2", level=100)
        with self.assertRaises(IntegrityError):
            Role.objects.create(name="Test Role 1 ", level=-1)

    def test_role_name_unique(self):
        Role.objects.create(name="Test Role 3", level=2)
        with self.assertRaises(IntegrityError):
            Role.objects.create(name="Test Role 3", level=2)

    def test_role_name_not_unique(self):
        with self.assertRaises(IntegrityError):
            Role.objects.create(name="Test Role", level=2)
