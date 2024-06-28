from rest_framework import serializers

from ..models import Branch
from .delivery_region_serializer import DeliveryRegionSerializer


class BranchSerializer(serializers.ModelSerializer):
    delivery_regions = DeliveryRegionSerializer(many=True, read_only=True)

    class Meta:
        model = Branch
        fields = [
            "id",
            "display_name",
            "delivery_regions",
            "pickup_locations",
            "frequency_of_requests",
            "spay_neuter_requirement",
            "pets_per_household_max",
            "delivery_deadline_days",
            "delivery_type",
            "delivery_pickup_details",
            "blurb",
            "blurb_image",
            "latitude",
            "longitude",
            "delivery_radius",
            # Updated fields from PhysicalLocationMixin
            "location_name",
            "address_line1",
            "address_line2",
            "city",
            "state_or_province",
            "postal_code",
            "country",
            "ext_id",
        ]
        read_only_fields = ["id"]

    # ... rest of the serializer code remains the same

    def validate_delivery_radius(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError(
                "Delivery radius must be greater than 0."
            )
        return value

    def validate_pets_per_household_max(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Maximum pets per household must be greater than 0."
            )
        return value

    def validate_delivery_deadline_days(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Delivery deadline days must be greater than 0."
            )
        return value

    def validate(self, data):
        if data.get("latitude") is not None and data.get("longitude") is None:
            raise serializers.ValidationError(
                "Both latitude and longitude must be provided together."
            )
        if data.get("latitude") is None and data.get("longitude") is not None:
            raise serializers.ValidationError(
                "Both latitude and longitude must be provided together."
            )
        return data
