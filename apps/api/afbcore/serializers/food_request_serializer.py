from rest_framework import serializers

from ..models import FoodRequest, Pet
from .pet_serializer import PetSerializer


class ClientPetsSerializer(serializers.Serializer):
    pets = PetSerializer(many=True)


class DeliveryContactSerializer(serializers.Serializer):
    choose_contact = serializers.BooleanField()
    contact_name = serializers.CharField()
    preferred_method = serializers.CharField()
    contact_phone = serializers.CharField()


class ConfirmationSerializer(serializers.Serializer):
    confirm_info = serializers.BooleanField()
    accept_terms = serializers.BooleanField()


class SafeDropSerializer(serializers.Serializer):
    confirm = serializers.BooleanField()
    instructions = serializers.CharField()


class AbstractFoodRequestSerializer(serializers.ModelSerializer):
    method_of_contact = serializers.CharField()
    delivery_contact = DeliveryContactSerializer()

    contact_phone = serializers.CharField()

    client_pets = ClientPetsSerializer()
    confirmation = ConfirmationSerializer()
    safe_drop = SafeDropSerializer()

    class Meta:
        abstract = True
        model = FoodRequest
        fields = [
            "id",
            "user",
            "pets",
            "branch",
            "address_text",
            "address_google_place_id",
            "address_canadapost_id",
            "address_latitude",
            "address_longitude",
            "address_buildingtype",
            "address_details",
            "ext_address_details",
            "address_instructions",
            "contact_phone",
            "contact_email",
            "contact_name",
            "method_of_contact",
            "safe_drop_agree",
            "safe_drop_instructions",
            "confirm_correct",
            "accept_terms",
            "flagged",
            "date_requested",
            "request_status",
            "comments",
            "created",
            "modified",
        ]


class FoodRequestCreateSerializer(AbstractFoodRequestSerializer):
    class Meta(AbstractFoodRequestSerializer.Meta):
        read_only_fields = ["id", "created", "modified"]


class FoodRequestUpdateSerializer(AbstractFoodRequestSerializer):
    class Meta(AbstractFoodRequestSerializer.Meta):
        read_only_fields = [
            "id",
            "user",
            "branch",
            "created",
            "address_canadapost_id",
            "address_google_place_id",
            "address_latitude",
            "address_longitude",
            "address_buildingtype",
            "address_details",
            "request_status",
        ]
