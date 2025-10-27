from unittest import skip

from afbcore.models.branch import Branch
from afbcore.models.delivery_region import DeliveryRegion
from afbcore.models.users.profile import Profile
from django.contrib.auth import get_user_model
from django.test import TestCase

"""
    Run these tests with the following command:
    python manage.py test afbcore.tests.models.test_profile
"""


class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.User = get_user_model()
        cls.Branch = Branch.objects.create(display_name="Test Branch")
        cls.DeliveryRegion = DeliveryRegion.objects.create(
            name="Test Delivery Region"
        )

        cls.user = cls.User.objects.create_user(
            name="testuser",
            email="testuser@example.com",
            password="testpass123",
        )

        cls.profile = Profile.objects.create(
            user=cls.user,
            preferred_name="Plop",
            phone_number="+1234567890",
            address_verbatim="123 Main St",
            address="123 Main St",
            validated_postal_code="12345",
            country="USA",
            status="active",
            branch=cls.Branch,
        )

        cls.profile.delivery_regions.add(cls.DeliveryRegion)

    def test_profile_user_relation(self):
        profile = Profile.objects.get(id=self.profile.id)
        self.assertEqual(profile.user, self.user)

    def test_profile_branch_relation(self):
        profile = Profile.objects.get(id=self.profile.id)
        self.assertEqual(profile.branch, self.Branch)

    def test_profile_delivery_regions_relation(self):
        profile = Profile.objects.get(id=self.profile.id)
        self.assertEqual(profile.delivery_regions.count(), 1)
        self.assertEqual(profile.delivery_regions.first(), self.DeliveryRegion)

    def test_profile_str_method(self):
        profile = Profile.objects.get(id=self.profile.id)
        self.assertEqual(str(profile), "Plop")
