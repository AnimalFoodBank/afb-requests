# All imports are grouped at the top
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Get the User model
User = get_user_model()


# UserSerializer class
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "url", "username", "email", "is_staff"]
        extra_kwargs = {
            "url": {"view_name": "user-detail"},
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User(email=validated_data["email"], username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user
