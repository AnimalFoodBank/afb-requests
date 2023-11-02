import uuid
from django.db import models


class DeliveryRegion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(
        max_length=255, help_text="Name of the region (e.g. postal code, city, or area)"
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    pet_request = models.ForeignKey("Request", on_delete=models.DO_NOTHING)

    food_available = models.ForeignKey("FoodAvailable", on_delete=models.DO_NOTHING)

    delivery_date = models.DateField()
    delivery_time = models.TimeField()

    delivery_address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.client} - {self.delivery_date}"
