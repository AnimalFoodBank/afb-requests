from rest_framework import serializers


class PhysicalLocationSerializerMixin(serializers.Serializer):
    location_name = serializers.CharField(max_length=50)
    address_line1 = serializers.CharField(
        max_length=100, allow_null=True, required=False
    )
    address_line2 = serializers.CharField(
        max_length=100, allow_null=True, required=False
    )
    city = serializers.CharField(max_length=50, allow_null=True, required=False)
    state_or_province = serializers.CharField(
        max_length=50, allow_null=True, required=False
    )
    postal_code = serializers.CharField(
        max_length=16, allow_null=True, required=False
    )
    country = serializers.CharField(
        max_length=50, allow_null=True, required=False
    )
    instructions = serializers.CharField(
        max_length=50, allow_null=True, required=False
    )
    ext_id = serializers.CharField(
        max_length=255, allow_null=True, required=False
    )

    class Meta:
        fields = [
            "location_name",
            "address_line1",
            "address_line2",
            "city",
            "state_or_province",
            "postal_code",
            "country",
            "ext_id",
        ]
