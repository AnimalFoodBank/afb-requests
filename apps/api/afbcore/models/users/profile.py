import uuid

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from ..base import BaseAbstractModel
from ..mixins import HasDetailsMixin

# Profile depends on User and not the other way around
from .user import User  # noqa: F401

# Status - Active, On Hold, Banned
STATUS_CHOICES = [
    ("active", "Active"),
    ("on_hold", "On Hold"),
    ("banned", "Banned"),
    # Add to the end of the list to avoid breaking existing code
]

# Define default arguments for ManyToManyField
MANY_TO_MANY_DEFAULTS = {
    "related_name": "+",
    "blank": True,
    "symmetrical": False,
}

ROLE_CHOICES = [
    ("client", "Client"),
    ("volunteer", "Volunteer"),
    ("manager", "Manager"),
    ("admin", "Admin"),
]


class Profile(HasDetailsMixin, BaseAbstractModel):
    """
    A model representing a user profile.

    Fields:
    - id: UUIDField, primary key
    - user: ForeignKey to User model
    - role: OneToOneField to Role model
    - branches: ManyToManyField to Branch model
    - preferred_name: CharField, max length 64
    - email: EmailField, unique
    - phone_number: PhoneNumberField, max length 20, region US
    - address_verbatim: CharField, max length 255, blank
    - address: CharField, max length 255, null
    - delivery_regions: ManyToManyField to DeliveryRegion model
    - validated_postal_code: CharField, max length 20, null
    - country: CharField, max length 255, blank
    - status: CharField, max length 20, choices STATUS_CHOICES, default "active"

    About profiles:
    We need to do our best to ensure each account is unique. Clients
    try to subvert and create duplicate accounts to circumvent frequency,
    change number of pets, etc.

    """

    class Meta:
        ordering = ["-created"]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="profiles"
    )

    # Usually just one, but can be multiple
    branch = models.ForeignKey(
        "Branch",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="profiles",
    )

    # Name fields
    preferred_name = models.CharField(max_length=64, null=True)

    # Phone - Validate format - numbers only
    phone_number = PhoneNumberField(region="CA", null=True)

    # We allow free form text entry but store the validated
    # address in the `address` field. These fields should
    # generally be updated together.
    #
    # e.g. A client may enter "123 Main St" and another
    # client may enter "123 Main Street"
    address_verbatim = models.CharField(max_length=255, blank=True, null=True)

    # Validated Address
    # i.e. An address from Canada Post or Google Maps
    address = models.CharField(max_length=255, blank=True, null=True)

    # An open-ended field for additional address details if needed
    address_details = models.JSONField(default=dict)

    # Used to store the google places `PlaceResult` object.
    #
    # e.g. { 'place': { 'place_id': 'ChIJd8BlQ2BZwokRAFUEcm_qrcA', 'formatted_address': '123 Main St, Winnipeg, MB R3C 1A5, Canada', 'geometry': { 'location': { 'lat': 49.895077, 'lng': -97.138451 }, 'viewport': { 'northeast': { 'lat': 49.89642582989272, 'lng': -97.13710217010728 }, 'southwest': { 'lat': 49.89372617010728, 'lng': -97.13980182989273 } } }, 'name': '123 Main St', 'types': [ 'street_address' ] }
    #
    ext_address_details = models.JSONField(default=dict)

    role = models.CharField(
        _("role"),
        choices=ROLE_CHOICES,
        max_length=255,
        default="client",
    )

    #
    # Via Volunteer
    #

    # Postal/Zip Codes/Cities will deliver to
    # We will use this to notify them of available deliveries in their "regions"
    delivery_regions = models.ManyToManyField(
        "DeliveryRegion", related_name="delivery_regions"
    )

    #
    # Via Client
    #

    # Address - If address is duplicate to another clients, both accounts
    # need to be placed on hold and manually reviewed/approved bc people
    # are scammers. Has to be a validated address (google?) and notWHich modela
    # permitted to be overwritten. The last amount of free form text
    # entry as possible. You'd be amazed how many clients don't know
    # their postal code and we route by postal code sooooo
    #
    # Postal/Zip Code - Has to be a validated address (google?) and not
    # permitted to be overwritten. The last amount of free form text
    # entry as possible. You'd be amazed how many clients don't know
    # their postal code and we route by postal code sooooo
    #
    validated_postal_code = models.CharField(max_length=20, null=True)

    # Country - I don't know if we need this but google addresses populate country too. It may be useful for analytics
    country = models.CharField(max_length=255, blank=True)

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="active"
    )

    def __str__(self):
        return f"{self.preferred_name}"
