from .user_serializer import UserSerializer  # noqa


from rest_framework import serializers
from ..models import Request


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = [
            "profile",
            "branch",
            "pets",
            "confirm_address",
            "confirm_phone_number",
            "method_of_contact",
            "food_types_available",
            "date_requested",
            "safe_drop",
            "request_notes",
            "status",
            "driver_comments",
            "picture_of_delivery",
            "needs_review",
            "created",
            "modeified",
            "is_removed",
        ]
