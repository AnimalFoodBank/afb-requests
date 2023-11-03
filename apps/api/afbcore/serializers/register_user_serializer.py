# All imports are grouped at the top
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Get the User model
User = get_user_model()


class RegisterUserSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a new user.

    This serializer is used to create a new user account, and it includes fields for the user's email,
    username, and password. It also includes optional fields for the user's first and last name.

    This serializer is separate from the `UserSerializer` because it includes additional fields that are
    required for user registration, but are not necessarily needed for other operations on the user model.

    Fields:
    - email: EmailField, required
    - password: CharField, write_only, required
    - password2: CharField, write_only, required
    - username: CharField, required
    - first_name: CharField, not required
    - last_name: CharField, not required
    """

    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.only("email"))]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "password2",
            "email",
            "first_name",
            "last_name",
        )
        extra_kwargs = {
            "first_name": {"required": False},
            "last_name": {"required": False},
            "username": {"required": True},
            "email": {"required": True},
            "password": {"write_only": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
