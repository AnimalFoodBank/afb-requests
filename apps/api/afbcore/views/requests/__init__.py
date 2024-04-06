from rest_framework import exceptions, viewsets

from ...models import FoodRequest
from ...serializers import FoodRequestSerializer

# TODO: Add permissions and authentication to this viewset.
# This is a public endpoint, so we don't need any special permissions or
# authentication.


class FoodRequestViewSet(viewsets.ModelViewSet):
    queryset = (
        FoodRequest.objects.all()
    )  # TODO: Limit scope (60 days -> not deleted etc)
    serializer_class = FoodRequestSerializer
    lookup_field = "id"

    def destroy(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed("DELETE")
