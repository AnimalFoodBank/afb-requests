from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import Branch
from ..serializers import BranchSerializer


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "operational",
        "hidden",
        "delivery_type",
        "spay_neuter_requirement",
    ]
    search_fields = [
        "display_name",
        "location_name",
        "city",
        "state_or_province",
        "country",
    ]
    ordering_fields = [
        "display_name",
        "location_name",
        "city",
        "state_or_province",
        "country",
    ]

    def get_queryset(self):
        """
        Optionally restricts the returned branches to non-hidden ones,
        by filtering against a `show_hidden` query parameter in the URL.
        """
        queryset = Branch.objects.all()
        show_hidden = self.request.query_params.get("show_hidden", None)
        if show_hidden is None or show_hidden.lower() != "true":
            queryset = queryset.filter(hidden=False)
        return queryset

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()
