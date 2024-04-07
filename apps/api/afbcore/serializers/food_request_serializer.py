from rest_framework import serializers

from ..models import FoodRequest


class FoodRequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodRequest
        fields = [
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
            "pet_details",
            "confirm_correct",
            "accept_terms",
            "date_requested",
        ]
        read_only_fields = [
            "id",
            "user",
            "branch",
            "created",
            "modified",
            "address_canadapost_id",
            "address_google_place_id",
            "pet_details",
        ]


class FoodRequestUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodRequest
        fields = [
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
            "pet_details",
            "confirm_correct",
            "accept_terms",
            "date_requested",
        ]
        read_only_fields = [
            "id",
            "user",
            "branch",
            "created",
            "address_canadapost_id",
            "address_google_place_id",
            "pet_details",
        ]
