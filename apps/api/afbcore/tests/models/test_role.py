from django.test import TestCase
from afbcore.models.users.role import Role

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
        self.assertEqual(role.level, 1)

    def test_role_str_method(self):
        role = Role.objects.get(id=self.role.id)
        self.assertEqual(str(role), "Test Role")

    def test_role_name_required(self):
        with self.assertRaises(ValueError):
            Role.objects.create(level=1)

    def test_role_level_range(self):
        with self.assertRaises(ValueError):
            Role.objects.create(name="Test Role", level=-1)

        with self.assertRaises(ValueError):
            Role.objects.create(name="Test Role", level=100)

    def test_role_name_unique(self):
        with self.assertRaises(Exception):
            Role.objects.create(name="Test Role", level=2)
