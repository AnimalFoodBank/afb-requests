from ..models import DeliveryRegion
from .mixins import PhysicalLocationSerializerMixin


class DeliveryRegionSerializer(PhysicalLocationSerializerMixin):
    class Meta:
        model = DeliveryRegion
        fields = [
            "id",
            "name",
            "description",
        ] + PhysicalLocationSerializerMixin.Meta.fields
