import uuid

from django.db import models

from .base import BaseAbstractModel
from .mixins import HasDetailsMixin, PhysicalLocationMixin

"""
    Run these tests with the following command:
    python manage.py test afbcore.tests.models.test_delivery_region

"""


class DeliveryRegion(PhysicalLocationMixin, HasDetailsMixin, BaseAbstractModel):
    """
    Represents a delivery region with an address.

    e.g. Postal/Zip Codes/Cities that a Volunteer will deliver to. This
    could be a single postal code, a city, or a region.

    We allow free form text entry but store the validated
    address in the `address` field if we're able to validate it. This is
    intentionally open ended to replicate the wild west data entry that
    happens in the real world.

    TODO: Figure out how to do this. It could be a list of strings as a
    rudimentary approach, where the string could be a postal code, city,
    or region. Or it could be a list of foreign keys to a "DeliveryRegion"
    which would still be a simple string but reduce dupes.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(
        max_length=255,
        help_text="Name of the region (e.g. postal code, city, or area)",
    )
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def has_useable_address(self):
        """
        Returns True if the address is not None and not an empty string.

        `bool` returns True if self.address is not None and not an empty string,
        and False otherwise. The bool function in Python returns False for None
        and empty sequences or collections (including strings), and True for
        non-empty sequences or collections.
        """
        return bool(self.name)
