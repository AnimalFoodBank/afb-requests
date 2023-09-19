
import uuid
from django.db import models

class Volunteer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

    # Would love for the client and volunteer to be able to communicate through the software - and not have the volunteer have to use their personal phone to arrange delivery.  However, we, as admin, need their phone number
    phone_number = models.CharField(max_length=20)

    # Postal/Zip Codes/Cities will deliver to
    # We will use this to notify them of available deliveries in their "regions"
    # TODO: Figure out how to do this
    delivery_regions = models.ManyToManyField("DeliveryRegion")

    # Points/Rewards Earned
    # For each delivery made/attempted - redeem these for swag/gift cards
    points_earned = models.IntegerField(default=0)


    def __str__(self):
      return f"{self.first_name} {self.last_name}"
