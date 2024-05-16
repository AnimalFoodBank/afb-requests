from rest_framework import serializers

from ..models import FoodRequest


class FoodRequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodRequest
        fields = [
            "id",
            "user",
            "branch",
            "created",
            "modified",
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
            "safe_drop_agree",
            "safe_drop_instructions",
            "status",
        ]
        read_only_fields = [
            "id",
            # Note about adding fields here in the create
            # serializer: only fields that should be populated
            # by our code or the database should be included
            # here. Including "user" here for example, would
            # prevent the UUID value from making it into
            # the database -- leading to a NULL error
            # since a request must have a user.
            "status",
        ]


class FoodRequestUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodRequest
        fields = [
            "id",
            "user",
            "branch",
            "created",
            "modified",
            "address_canadapost_id",
            "address_google_place_id",
            "pet_details",
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
            "safe_drop_agree",
            "safe_drop_instructions",
            "status",
        ]
        read_only_fields = [
            "id",
            "user",
            "branch",
            "created",
            "address_canadapost_id",
            "address_google_place_id",
            "pet_details",
            "status",
        ]
