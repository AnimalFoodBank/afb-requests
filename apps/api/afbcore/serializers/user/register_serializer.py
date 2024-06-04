import uuid

from django.contrib.auth.hashers import make_password

from .user_serializer import UserSerializer


class RegisterSerializer(UserSerializer):
    def create(self, validated_data):
        # Generate a random UUID
        password = uuid.uuid4().hex

        # Hash the password
        hashed_password = make_password(password)

        # Set the password in the validated_data dictionary
        validated_data["password"] = hashed_password

        # Call the superclass's create method
        return super().create(validated_data)
