from rest_framework import serializers

from ..models import Pet


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = [
            "id",
            "pet_name",
            "pet_type",
            "pet_dob",
            "profile",
            "food_details",
            "dog_details",
            "created",
            "modified",
        ]
        read_only_fields = ["created", "modified", "id"]
