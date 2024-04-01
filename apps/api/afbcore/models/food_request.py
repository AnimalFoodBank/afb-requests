# PetRequest

import uuid

from django.db import models
from model_utils import Choices
from phonenumber_field.modelfields import PhoneNumberField

from .base import BaseAbstractModel

STATUS_CHOICES = [
    ("received", "Request Received"),
    ("approved", "Request Approved & in Queue"),
    ("denied", "Request Denied"),
    ("assigned", "Volunteer Assigned"),
    ("ready_for_pickup", "Request Ready For Volunteer Pickup"),
    ("scheduled", "Delivery Scheduled"),
    ("out_for_delivery", "Out For Delivery"),
    ("delivered", "Delivered"),
    ("undeliverable", "Undeliverable"),
]

BUILDING_TYPE_CHOICES = Choices(
    ("HOUSE", "House"),
    ("APARTMENT", "Apartment"),
    ("TOWNHOUSE", "Townhouse"),
    ("CONDO", "Condo"),
    ("LANEWAY", "Laneway"),
    ("DETACHED_HOUSE", "Detached house"),
    ("OTHER", "Other"),
    ("NOT_SPECIFIED", "Not specified"),
)


class FoodRequest(BaseAbstractModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # TODO: Should this be a foreign key to the user model? A user can have
    # multiple profiles, so we need to think about this.
    user = models.ForeignKey("User", on_delete=models.DO_NOTHING)

    # A food request can belong to only one Branch
    branch = models.ForeignKey("Branch", on_delete=models.DO_NOTHING, null=True)

    address_text = models.TextField(null=True, blank=True)
    address_google_place_id = models.CharField(max_length=255, blank=True, null=True)
    address_canadapost_id = models.CharField(max_length=255, blank=True, null=True)
    address_latitude = models.FloatField(blank=True, null=True, default=0)
    address_longitude = models.FloatField(blank=True, null=True, default=0)
    address_buildingtype = models.CharField(
        max_length=100,
        choices=BUILDING_TYPE_CHOICES,
        default=BUILDING_TYPE_CHOICES.NOT_SPECIFIED,
    )
    address_details = models.JSONField(default=dict)

    # A PhoneNumberField, which is a custom field provided by the 'phonenumber_field' library. It stores a phone number in a standardized format and includes region-specific validation. The 'region' parameter is set to "CA" to indicate that the phone number should be formatted according to Canadian standards.
    contact_phone = PhoneNumberField(region="CA", blank=True)

    # An EmailField, which is a built-in field provided by Django. It stores an email address and performs basic email validation.
    contact_email = models.EmailField(blank=True)

    # Someone else may be there for the food delivery, or they may prefer a different name.
    contact_name = models.CharField(max_length=100)

    # Preferred way for us to contact them about the request Email, Text or Phone
    method_of_contact = models.CharField(max_length=100)

    # TODO: Pet
    # One or more.
    # ** We will want them to see and confirm/edit their address and phone number on the request, and be able to see pets, and edit some fields of their pets info
    pets = models.ManyToManyField("Pet", default=list, null=True)  # uuid expected

    # Safe drop - if they are not home, can we leave the food at the door?
    # Yes/No
    safe_drop_agree = models.BooleanField(null=True, blank=True)
    safe_drop_instructions = models.TextField(max_length=255, null=True, blank=True)

    # Yes/No -
    # No requires them to edit address in the UI so in theory this should
    # always be True. Note: we need to ensure that it's not attached to
    # another client or then both clients need to be on hold to review.
    confirm_correct = models.BooleanField()

    # Yes/No - No requires them to update phone number (validate format)
    accept_terms = models.BooleanField()

    # Not sure what to call this one, but if the volunteer has an issue with the client - they are rude or aggressive for example, can we allow the driver to mark the client as suspended and admin to review? (was "needs review"). Maybe an enum would be more appropriate here? Although that would dilute status a bit.
    highlighted = models.BooleanField()

    # Use system date - do not let clients input/edit.  We like to have deliveries made within the branches delivery window so would be great if we could send notifications when requests are "aging"
    date_requested = models.DateField(auto_now_add=True)

    # Request Received, Request Approved & in Queue, Request Denied, Volunteer Assigned, Request Ready For Volunteer Pickup, Delivery Scheduled, Out For Delivery, Delivered, Undeliverable
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="received")

    # Free form comments from driver, client, volunteer, etc.
    comments = models.JSONField(default=dict)

    def __str__(self):
        return f"Food Request {self.id}"

    class Meta:
        ordering = ["-date_requested"]
