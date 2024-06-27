import pytest
from afbcore.models import (
    Profile,
)
from afbcore.serializers import ProfileSerializer
from django.contrib.auth import get_user_model

# from pytest_mock import mocker
from rest_framework import serializers

User = get_user_model()

"""
    To run this test, run the following command:
    pnpm django test apps/api/afbcore/tests/serializers/test_profile_serializer_meta.py
    pytest apps/api/afbcore/tests/serializers/test_profile_serializer_meta.py
"""

# re: generating tests, some custom instructions for codiumate
# List imports outside of the test function; Don't create any new classes; Don't use mocker or unittest. Use only pytest features.


class TestProfileSerializerMeta:
    def test_meta_fields(self):
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
        fields = ProfileSerializer.Meta.fields
        assert set(fields) == set(
            expected_fields
        ), "Meta fields do not match expected fields"

    def test_meta_read_only_fields(self):
        expected_read_only_fields = [
            "id",
            "user",
            "status",
            "country",
            "role",
            "delivery_regions",
        ]
        read_only_fields = ProfileSerializer.Meta.read_only_fields
        assert set(read_only_fields) == set(
            expected_read_only_fields
        ), "Meta read-only fields do not match expected read-only fields"

    def test_meta_model_class(self):
        assert (
            ProfileSerializer.Meta.model == Profile
        ), "Meta model does not match the Profile model"

    @pytest.mark.django_db
    def test_create_and_update_profile_valid_data_with_django_db_mark(self):
        self.user = User.objects.create(username="testuser")
        initial_data = {
            "preferred_name": "John",
            "phone_number": "+123456789",
            "address_verbatim": "123 Main St",
            "address": "123 Main Street",
            "role": "client",
        }
        profile = Profile.objects.create(user=self.user, **initial_data)

        new_preferred_name = "Jane"
        profile.preferred_name = new_preferred_name
        profile.save()

        updated_profile = Profile.objects.get(id=profile.id)
        assert (
            updated_profile.preferred_name == new_preferred_name
        ), "Profile was not updated successfully"

    @pytest.mark.django_db
    @pytest.mark.skip
    def test_create_profile_with_invalid_address_format_fixed(self):
        def validate_address(address):
            raise NotImplementedError("validate address")

        user = User.objects.create(username="testuser")
        invalid_address = {
            "address_verbatim": "123 Main St",
            "address": "Invalid Address Format",
        }
        profile = Profile.objects.create(user=user, **invalid_address)

        validated_address = validate_address(profile.address)

        assert (
            validated_address is None
        ), "Address was validated with invalid format"

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

    # Meta class correctly maps to Profile model
    def test_meta_class_maps_to_profile_model(self):
        assert ProfileSerializer.Meta.model == Profile

    # Handling of missing optional fields in input data
    def test_handling_missing_optional_fields(self):
        class MockProfileSerializer(serializers.ModelSerializer):
            class Meta(ProfileSerializer.Meta):
                pass

        input_data = {
            "user": 1,
            "preferred_name": "John Doe",
            "phone_number": "+17784567890",
            "address_verbatim": "123 Main St",
            "address": "123 Main St",
            "role": "client",
            "validated_postal_code": "12345",
        }

        serializer = MockProfileSerializer(data=input_data)
        assert serializer.is_valid(), serializer.errors
