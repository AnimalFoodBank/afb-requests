from django.test import TestCase
from django.contrib.auth import get_user_model
from afbcore.models.users.profile import Profile
from afbcore.models.users.role import Role
from afbcore.models.branch import Branch
from afbcore.models.delivery_region import DeliveryRegion

"""
    Run these tests with the following command:
    python manage.py test afbcore.tests.models.test_profile
"""


class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.User = get_user_model()
        cls.Role = Role.objects.create(name="Test Role")
        cls.Branch = Branch.objects.create(name="Test Branch")
        cls.DeliveryRegion = DeliveryRegion.objects.create(name="Test Delivery Region")

        cls.user = cls.User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass123",
        )

        cls.profile = Profile.objects.create(
            user=cls.user,
            role=cls.Role,
            first_name="Test",
            last_name="User",
            email="testuser@example.com",
            phone_number="+1234567890",
            address_verbatim="123 Main St",
            address="123 Main St",
            validated_postal_code="12345",
            country="USA",
            status="active",
        )

        cls.profile.branches.add(cls.Branch)
        cls.profile.delivery_regions.add(cls.DeliveryRegion)

    def test_profile_user_relation(self):
        profile = Profile.objects.get(id=self.profile.id)
        self.assertEqual(profile.user, self.user)

    def test_profile_role_relation(self):
        profile = Profile.objects.get(id=self.profile.id)
        self.assertEqual(profile.role, self.Role)

    def test_profile_branches_relation(self):
        profile = Profile.objects.get(id=self.profile.id)
        self.assertEqual(profile.branches.count(), 1)
        self.assertEqual(profile.branches.first(), self.Branch)

    def test_profile_delivery_regions_relation(self):
        profile = Profile.objects.get(id=self.profile.id)
        self.assertEqual(profile.delivery_regions.count(), 1)
        self.assertEqual(profile.delivery_regions.first(), self.DeliveryRegion)

    def test_profile_str_method(self):
        profile = Profile.objects.get(id=self.profile.id)
        self.assertEqual(str(profile), "Test User")

    def test_profile_absolute_url_method(self):
        profile = Profile.objects.get(id=self.profile.id)
        self.assertEqual(profile.get_absolute_url(), f"/clients/create/{profile.id}/")
