# PetRequest

import uuid

from django.db import models


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


class Request(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # TODO: Should this be a foreign key to the user model? A user can have
    # multiple profiles, so we need to think about this.
    profile = models.ForeignKey("Profile", on_delete=models.DO_NOTHING)

    # A food request can belong to only one Branch
    branch = models.ForeignKey("Branch", on_delete=models.DO_NOTHING)

    # One or more.
    # ** We will want them to see and confirm/edit their address and phone number on the request, and be able to see pets, and edit some fields of their pets info
    pets = models.ManyToManyField("Pet")

    # Yes/No -
    # No requires them to edit address in the UI so in theory this should
    # always be True. Note: we need to ensure that it's not attached to
    # another client or then both clients need to be on hold to review.
    confirm_address = models.BooleanField()

    # Yes/No - No requires them to update phone number (validate format)
    confirm_phone_number = models.BooleanField()

    # Text or Phone
    method_of_contact = models.CharField(max_length=100)

    # Drop down list with an "other" option that is free form text.  Select all that apply.
    food_types_available = models.ManyToManyField("FoodAvailable")

    # Use system date - do not let clients input/edit.  We like to have deliveries made within the branches delivery window so would be great if we could send notifications when requests are "aging"
    date_requested = models.DateField(auto_now_add=True)

    # Yes/No
    safe_drop = models.BooleanField()

    # Free form comments from client - set max character limit
    request_notes = models.TextField(max_length=255)

    # Request Received, Request Approved & in Queue, Request Denied, Volunteer Assigned, Request Ready For Volunteer Pickup, Delivery Scheduled, Out For Delivery, Delivered, Undeliverable
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="received")

    # Driver comments
    driver_comments = models.TextField(max_length=255, null=True, blank=True)

    # Picture of delivery
    picture_of_delivery = models.ImageField(
        upload_to="delivery_pictures/", null=True, blank=True
    )

    # Not sure what to call this one, but if the volunteer has an issue with the client - they are rude or aggressive for example, can we allow the driver to mark the client as suspended and admin to review?
    needs_review = models.BooleanField()

    def __str__(self):
        return f"Pet Request {self.id}"

    class Meta:
        ordering = ["-date_requested"]
