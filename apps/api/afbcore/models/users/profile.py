import uuid

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from django.urls import reverse

from .role import Role
from .user import User  # Profile depends on User and not the other way around

from ..base import BaseAbstractModel

# Status - Active, On Hold, Banned
STATUS_CHOICES = [
    ("active", "Active"),
    ("on_hold", "On Hold"),
    ("banned", "Banned"),
]


# Define default arguments for ManyToManyField
MANY_TO_MANY_DEFAULTS = {
    "related_name": "+",
    "blank": True,
    "symmetrical": False,
}


class Profile(BaseAbstractModel):
    """
    A model representing a user profile.

    Fields:
    - id: UUIDField, primary key
    - user: ForeignKey to User model
    - role: OneToOneField to Role model
    - branches: ManyToManyField to Branch model
    - first_name: CharField, max length 64
    - last_name: CharField, max length 64
    - email: EmailField, unique
    - phone_number: PhoneNumberField, max length 20, region US
    - address_verbatim: CharField, max length 255, blank
    - address: CharField, max length 255, null
    - delivery_regions: ManyToManyField to DeliveryRegion model
    - points_earned: IntegerField, default 0
    - validated_postal_code: CharField, max length 20, null
    - country: CharField, max length 255, blank
    - status: CharField, max length 20, choices STATUS_CHOICES, default "active"

    About profiles:
    We need to do our best to ensure each account is unique. Clients
    try to subvert and create duplicate accounts to circumvent frequency,
    change number of pets, etc.

    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # user = models.ForeignKey(
    #     User, on_delete=models.DO_NOTHING, related_name="pro2files"
    # )
    # role = models.ForeignKey(
    #     Role, on_delete=models.DO_NOTHING, related_name="prof2iles"
    # )

    # Usually just one, but can be multiple
    branches = models.ManyToManyField("Branch", **MANY_TO_MANY_DEFAULTS)

    # Name fields
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    # Email - Unique - don't allow duplicates.
    email = models.EmailField(unique=True)

    # Phone - Validate format - numbers only
    phone_number = PhoneNumberField(
        blank=True,
        null=True,
        region="US",
        max_length=20,
    )

    # We allow free form text entry but store the validated
    # address in the `address` field. These fields should
    # generally be updated together.
    #
    # e.g. A client may enter "123 Main St" and another
    # client may enter "123 Main Street"
    address_verbatim = models.CharField(max_length=255, blank=True)

    # Validated Address
    # i.e. An address from Canada Post or Google Maps
    address = models.CharField(max_length=255, null=True)

    #
    # Via Volunteer
    #

    # Postal/Zip Codes/Cities will deliver to
    # We will use this to notify them of available deliveries in their "regions"
    delivery_regions = models.ManyToManyField("DeliveryRegion")

    # Points/Rewards Earned
    # For each delivery made/attempted - redeem these for swag/gift cards
    points_earned = models.IntegerField(default=0)

    #
    # Via Client
    #

    # Address - If address is duplicate to another clients, both accounts need to be placed on hold and manually reviewed/approved bc people are scammers.
    # Has to be a validated address (google?) and not permitted to be overwritten. The last amount of free form text entry as possible.
    # You'd be amazed how many clients don't know their postal code and we route by postal code sooooo

    # Postal/Zip Code - Has to be a validated address (google?) and not permitted to be overwritten. The last amount of free form text entry as possible.
    # You'd be amazed how many clients don't know their postal code and we route by postal code sooooo
    validated_postal_code = models.CharField(max_length=20, null=True)

    # Country - I don't know if we need this but google addresses populate country too. It may be useful for analytics
    country = models.CharField(max_length=255, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("client-create", kwargs={"pk": self.pk})
