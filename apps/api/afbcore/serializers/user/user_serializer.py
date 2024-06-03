# All imports are grouped at the top
import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from drf_registration.api.user import UserSerializer as BaseUserSerializer
from rest_framework import serializers

# Get the User model
User = get_user_model()


# UserSerializer class
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Serialize as a plain string field to smooth out the
    # registration flow.
    phone = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ["id", "url", "name", "email", "phone", "is_staff"]
        extra_kwargs = {
            "url": {"view_name": "user-detail"},
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        # Generate a random UUID
        password = uuid.uuid4().hex

        # Hash the password
        hashed_password = make_password(password)

        # Set the password in the validated_data dictionary
        validated_data["password"] = hashed_password

        # Call the superclass's create method
        return super().create(validated_data)
