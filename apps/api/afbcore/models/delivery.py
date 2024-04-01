import uuid
from django.db import models


class Delivery(models.Model):
    food_request = models.ForeignKey("FoodRequest", on_delete=models.DO_NOTHING)

    food_available = models.ForeignKey("FoodAvailable", on_delete=models.DO_NOTHING)

    delivery_date = models.DateField()
    delivery_time = models.TimeField()

    delivery_address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.client} - {self.delivery_date}"
