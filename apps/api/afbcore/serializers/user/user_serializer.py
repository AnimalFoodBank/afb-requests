# All imports are grouped at the top
import logging
import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from drf_registration.api.user import UserSerializer as BaseUserSerializer
from rest_framework import serializers

logger = logging.getLogger(__name__)

# Get the User model
User = get_user_model()


# UserSerializer class
class UserSerializer(serializers.ModelSerializer):
    # Serialize as a plain string field to smooth out the
    # registration flow.
    phone = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ["id", "name", "email", "profile", "is_staff"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        # Generate a random UUID
        password = uuid.uuid4().hex

        # Add potential profile fields to details so that the
        # post_save signal will have access to them. This is
        # necessary because the profile is created after the
        # user is created.
        validated_data["details"] = {
            "role": validated_data.pop("role", None),
            "phone_number": validated_data.pop("phone_number", None),
        }

        # Hash the password
        hashed_password = make_password(password)

        # Set the password in the validated_data dictionary
        validated_data["password"] = hashed_password

        # Call the superclass's create method
        return super().create(validated_data)
