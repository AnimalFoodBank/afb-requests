from rest_framework import exceptions, status, viewsets
from rest_framework.response import Response

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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed("DELETE")
