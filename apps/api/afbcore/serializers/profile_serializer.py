from rest_framework import serializers

from ..models import Profile
from .delivery_region_serializer import DeliveryRegionSerializer
from .pet_serializer import PetSerializer


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    pets = PetSerializer(many=True, read_only=True, required=False)

    delivery_regions = DeliveryRegionSerializer(
        many=True, read_only=True, required=False
    )

    # Serialize as a plain string field to avoid unnecessary
    # friction when the format is not correct.
    phone_number = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "branch",
            "preferred_name",
            "phone_number",
            "address_verbatim",
            "address",
            "address_details",
            "ext_address_details",
            "role",
            "pets",  # pets are modified in their own serializer
            "delivery_regions",
            "validated_postal_code",
            "country",
            "status",
            "created",
            "modified",
        ]
        # depth = 1
        read_only_fields = [
            "id",
            "user",
            "status",
            "country",
            "pets",
            "role",
            "delivery_regions",
            "created",
        ]
