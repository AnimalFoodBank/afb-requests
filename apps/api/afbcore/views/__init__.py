# views/__init__.py

"""
This module contains the views for the AFB Core API application.

The views are responsible for handling HTTP requests and returning HTTP responses.
Each view corresponds to one or more URL patterns, and is responsible for handling
all HTTP methods (GET, POST, PUT, DELETE, etc.) that are allowed for that URL pattern.

This module also includes any helper functions or classes that are used exclusively
by the views in this module.
"""

from rest_framework import viewsets, exceptions

from ..models import FoodRequest
from ..serializers import RequestSerializer

from .users import UserViewSet  # noqa: F401


class FoodRequestViewSet(viewsets.ModelViewSet):
    queryset = FoodRequest.objects.all()  # TODO: Limit scope
    serializer_class = RequestSerializer
    lookup_field = "id"

    def destroy(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed("DELETE")
