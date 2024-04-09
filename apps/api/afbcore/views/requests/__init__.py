from rest_framework import exceptions, viewsets

from ...models import FoodRequest
from ...serializers import (
    FoodRequestCreateSerializer,
    FoodRequestUpdateSerializer,
)

# TODO: Add permissions and authentication to this viewset.
# This is a public endpoint, so we don't need any special permissions or
# authentication.


class FoodRequestViewSet(viewsets.ModelViewSet):
    queryset = FoodRequest.objects.all()
    lookup_field = "id"

    def get_serializer_class(self):
        if self.request.method == "POST":
            return FoodRequestCreateSerializer
        return FoodRequestUpdateSerializer

    def destroy(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed("DELETE")
