import uuid
from enum import Enum

from django.db import models
from django.db.models import JSONField

from .base import BaseAbstractModel
from .mixins import HasDetailsMixin


class PetSize(Enum):
    TOY = "Toy - up to 10lbs"
    SMALL_BREED = "Small Breed - 10-20 lbs"
    MEDIUM_BREED = "Medium Breed - 20-50 lbs"
    LARGE_BREED = "Large Breed - 50-100 lbs"
    GIANT_BREED = "Giant Breed - 100+ lbs"


class Pet(HasDetailsMixin, BaseAbstractModel):
    """
    Pet model to store information about pets belonging to a profile.

    The maximum number of pet profiles that would be allowed to be
    created would be deteremined from the Branch setting of "Number
    of Pet's Serviced/Houeshold". The default is 4.

    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    profile = models.ForeignKey(
        "Profile",
        on_delete=models.CASCADE,
        related_name="pets",
        null=True,
        blank=True,
    )

    pet_type = models.CharField(max_length=50)  # e.g. "dog", "cat", etc.
    pet_name = models.CharField(max_length=50)  # e.g. "Frankie"
    pet_dob = models.CharField(max_length=10)  # date of birth

    food_details = JSONField(default=dict)  # JSON blob
    dog_details = JSONField(default=dict)  # JSON blob
    animal_details = JSONField(default=dict)  # JSON blob
    spay_or_neutered = models.BooleanField(default=None, null=True)

    def save(self, *args, **kwargs):
        self.pet_type = self.pet_type.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return "%s (%s)" % (self.pet_name, self.pet_type)
