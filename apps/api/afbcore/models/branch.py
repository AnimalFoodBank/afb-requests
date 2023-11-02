import uuid

from django.db import models
from .mixins import PhysicalLocationMixin


class Branch(PhysicalLocationMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Location Name ie Winnipeg, MB; Medicine Hat, AB etc.
    location_name = models.CharField(
        max_length=255, help_text="ie Winnipeg, MB;  Medicine Hat, AB etc."
    )

    # Postal/Zip Code Range start with Canada but the intent is to
    # use this in the USA which may be more apt to paying
    # postal_zip_code_range = models.CharField(max_length=255)
    delivery_regions = models.ManyToManyField("DeliveryRegion")

    # Pickup Locations not sure about this one, but in Winnipeg for instance we have various spots to pick up inventory and those locations can change (they are volunteers houses). When drivers sign up for a delivery they choose the location they want to pick up from.
    pickup_locations = models.TextField(blank=True, null=True)

    # Frequency of Requests Weeks, Month, Months. This would need to be able
    # to be edited, as we do change it sometimes.
    frequency_of_requests = models.CharField(max_length=255)

    # Spay/Neuter Requirement likely a yes or no?  As in does that branch expect
    # clients to spay/neuter their pets to gain access to the food bank?
    spay_neuter_requirement = models.BooleanField(default=False)

    # Number of Pets serviced/Household. We set this as four but it may be nice, in future, to be able to edit it based on a regions bylaws.
    pets_per_household_max = models.IntegerField(default=4)

    # Delivery Deadline. For example, Winnipeg is 14 days
    delivery_deadline_days = models.IntegerField()

    # Delivery deadline in days
    delivery_deadline_days = models.IntegerField(default=3)

    # Type of delivery service, 'Drop off' or 'Pick up'
    # Delivery Type Drop off and/or pick up options
    delivery_type = models.CharField(
        max_length=24,
        choices=[("drop_off", "Drop off"), ("pick_up", "Pick up")],
        default="Drop off",
    )

    # Delivery/pickup More details
    delivery_pickup_details = models.TextField(blank=True)

    # Blurb An optional text field for a short intro or description etc.
    blurb = models.TextField(blank=True)

    # Blurb image A picture to go along with the blurb
    blurb_image = models.ImageField(upload_to="branch_images/", blank=True, null=True)
