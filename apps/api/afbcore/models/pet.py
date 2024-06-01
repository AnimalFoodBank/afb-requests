import uuid
from enum import Enum

from django.db import models
from django.db.models import JSONField


class PetSize(Enum):
    TOY = "Toy - up to 10lbs"
    SMALL_BREED = "Small Breed - 10-20 lbs"
    MEDIUM_BREED = "Medium Breed - 20-50 lbs"
    LARGE_BREED = "Large Breed - 50-100 lbs"
    GIANT_BREED = "Giant Breed - 100+ lbs"


class Pet(models.Model):

    """
    Pet model to store information about pets belonging to a profile.

    The maximum number of pet profiles that would be allowed
    to be created would be deteremined from the Branch
    setting of "Number of Pet's Serviced/Houeshold" above

    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    pet_type = models.CharField(max_length=50)  # e.g. "Dog", "Cat", etc.
    pet_name = models.CharField(max_length=50)  # e.g. "Frankie"
    pet_dob = models.CharField(max_length=10)  # date of birth

    food_details = JSONField(default=dict)  # JSON blob
    dog_details = JSONField(default=dict)  # JSON blob

    def __str__(self):
        return self.pet_name
