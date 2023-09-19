"""This module defines the FoodAvailable model."""

import uuid

from django.db import models
from enum import Enum

class PetType(Enum):
  CAT = 'Cat'
  DOG = 'Dog'
  OTHER = 'Other'


class FoodAvailable(models.Model):
    """
    Needs to support fields for different types of pets (e.g. cats, dogs, and other pets), as well as different types of food (e.g. dry and wet) and different amounts of food based on the size of the pet.

    Example of records that will need to be created.

        Cats
          Dry			1.25 lbs/cat/week
          Wet			6-12 cans if we have it
        Dogs
          Dry
          Toy			1.25 lbs/week
          Small Breed			3.5 lbs/week
          Medium Breed			6 lbs /week
          Large Breed			10 lbs/week
          Giant Breed			12.5 lbs/week
          Wet			6-12 cans if we have it

        Any other pet type				No estimate
        Total Cat Dry
        Total Cat Wet
        Total Dog Dry
        Total Dog Wet
     """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    pet_type = models.CharField(max_length=255, choices=[(pet_type.value, pet_type.value) for pet_type in PetType])
    food_type = models.CharField(max_length=255)
    food_amount = models.CharField(max_length=255)
