# All imports are grouped at the top
import logging
import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .profile_serializer import ProfileSerializer

logger = logging.getLogger(__name__)

# Get the User model
User = get_user_model()


# UserSerializer class
class UserSerializer(serializers.ModelSerializer):
    # A user can have multiple profiles
    profiles = ProfileSerializer(many=True)

    class Meta:
        model = User
        fields = ["id", "name", "email", "profiles", "is_staff"]
        read_only_fields = ["id", "is_staff", "profiles"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        # Add potential profile fields to details so that the
        # post_save signal will have access to them. This is
        # necessary because the profile is created after the
        # user is created.
        validated_data["details"] = {
            "role": validated_data.pop("role", None),
            "phone_number": validated_data.pop("phone_number", None),
        }

        # Use a randomly generated UUID in place of a password. This effectively
        # disables the password field for registration. Later on, the user will
        # be able to set their password. For now, we'll rely on magic links.
        password = uuid.uuid4().hex

        # Hash the password: convert the plain text to a value that can be
        # securely stored in the database. The critical feature of a hash
        # is that it only works in one direction. You can't take a hash
        # and convert it back to the original password.
        hashed_password = make_password(password)

        # Set the password in the validated_data dictionary
        validated_data["password"] = hashed_password

        # Call the superclass's create method
        return super().create(validated_data)
