from .user_serializer import UserSerializer  # noqa


from rest_framework import serializers
from ..models import FoodRequest


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodRequest
        fields = [
            "id",
            "user",
            "branch",
            "address_text",
            "address_google_place_id",
            "address_canadapost_id",
            "address_latitude",
            "address_longitude",
            "address_buildingtype",
            "address_details",
            "contact_phone",
            "contact_email",
            "contact_name",
            "method_of_contact",
            "pets",
            # "safe_drop_agree",
            # "safe_drop_instructions",
            "confirm_correct",
            "accept_terms",
            # "highlighted",
            "date_requested",
            # "status",
            # "comments",
            # Via BaseAbstractModel
            "created",
            "modified",
            "is_removed",
        ]
