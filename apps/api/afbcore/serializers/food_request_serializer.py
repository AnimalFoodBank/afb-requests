from rest_framework import serializers

from ..models import FoodRequest, Pet


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"


class ClientPetsSerializer(serializers.Serializer):
    which_pets = serializers.CharField()
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
        fields = [f.name for f in FoodRequest._meta.fields if f.name != "pets"]
        read_only_fields = ["id", "created_at", "updated_at"]


class FoodRequestCreateSerializer(AbstractFoodRequestSerializer):
    pass


class FoodRequestUpdateSerializer(serializers.ModelSerializer):
    read_only_fields = [
        "id",
        "user",
        "branch",
        "created",
        "address_canadapost_id",
        "address_google_place_id",
        "status",
    ]
