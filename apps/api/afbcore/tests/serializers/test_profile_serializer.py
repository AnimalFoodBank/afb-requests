import pytest
from afbcore.models import (
    Branch,
    DeliveryRegion,
    Profile,
)
from afbcore.models.mixins import HasDetailsMixin
from afbcore.serializers import DeliveryRegionSerializer, ProfileSerializer
from django.contrib.auth import get_user_model
from django.test import override_settings

# from pytest_mock import mocker
from rest_framework import serializers, status
from rest_framework.serializers import ListSerializer
from rest_framework.test import APITestCase

User = get_user_model()

"""
    To run this test, run the following command:

        $ pnpm django test apps/api/afbcore/tests/serializers/test_profile_serializer.py
        $ pytest apps/api/afbcore/tests/serializers/test_profile_serializer.py

    Or single test:
        $ pytest path/2/test_file.py::TestClass::test_func_name

"""


class TestProfileSerializer:
    @pytest.fixture
    def user(self):
        return User.objects.create(username="testuser")

    @pytest.fixture
    def profile_data(self, user):
        return {
            "user": user.id,
            "preferred_name": "John",
            "phone_number": "+123456789",
            "address_verbatim": "123 Main St",
            "address": "123 Main Street",
            "role": "client",
        }

    def test_profile_serializer_fields(self):
        serializer = ProfileSerializer()
        expected_fields = [
            "id",
            "user",
            "preferred_name",
            "phone_number",
            "address_verbatim",
            "address",
            "role",
            "delivery_regions",
            "validated_postal_code",
            "country",
            "status",
        ]
        assert set(serializer.fields.keys()) == set(
            expected_fields
        ), "Serializer fields do not match expected fields"

    def test_profile_serializer_read_only_fields(self):
        serializer = ProfileSerializer()
        expected_read_only_fields = [
            "id",
            "user",
            "status",
            "country",
            "role",
            "delivery_regions",
        ]
        assert set(serializer.Meta.read_only_fields) == set(
            expected_read_only_fields
        ), "Serializer read-only fields do not match expected read-only fields"

    def test_profile_serializer_model(self):
        serializer = ProfileSerializer()
        assert (
            serializer.Meta.model == Profile
        ), "Serializer model does not match the Profile model"

    from rest_framework.serializers import ListSerializer

    def test_profile_serializer_delivery_regions(self):
        serializer = ProfileSerializer()
        delivery_regions_field = serializer.fields["delivery_regions"]

        assert isinstance(
            delivery_regions_field, ListSerializer
        ), "delivery_regions field is not an instance of ListSerializer"

        assert isinstance(
            delivery_regions_field.child, DeliveryRegionSerializer
        ), "Elements in delivery_regions are not instances of DeliveryRegionSerializer"

    @pytest.mark.django_db
    def test_create_and_update_profile_valid_data(self, user, profile_data):
        print(user)
        # Ensure 'user' key is not in profile_data
        profile_data.pop(
            "user", None
        )  # Remove 'user' key if it exists, do nothing otherwise
        profile = Profile.objects.create(user=user, **profile_data)
        new_preferred_name = "Jane"
        profile.preferred_name = new_preferred_name
        profile.save()
        updated_profile = Profile.objects.get(id=profile.id)
        assert (
            updated_profile.preferred_name == new_preferred_name
        ), "Profile was not updated successfully"

    @pytest.mark.django_db
    def test_create_profile_without_user_error(self):
        with pytest.raises(Exception) as e:
            invalid_profile_data = {
                "preferred_name": "John",
                "phone_number": "+123456789",
                "address_verbatim": "123 Main St",
                "address": "123 Main Street",
                "role": "client",
            }
            Profile.objects.create(**invalid_profile_data)
        assert (
            str(e.value)
            == "NOT NULL constraint failed: afbcore_profile.user_id"
        ), "Expected error message not raised"
