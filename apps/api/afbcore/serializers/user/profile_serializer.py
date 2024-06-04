from rest_framework import serializers

from ...models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "preferred_name",
            "phone_number",
            "address_verbatim",
            "address",
            "role",
            "delivery_regions",
            "validated_postal_code",
            "country",
            "status",
        ]
        depth = 1
        read_only_fields = ["id", "user", "status", "country"]
