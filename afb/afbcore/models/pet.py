
from enum import Enum
from django.db import models

"""
The maximum number of pet profiles that would be allowed to be created would be deteremined from the Branch's setting of "Number of Pet's Serviced/Houeshold" above
"""

class PetSize(Enum):
    TOY = "Toy - up to 10lbs"
    SMALL_BREED = "Small Breed - 10-20 lbs"
    MEDIUM_BREED = "Medium Breed - 20-50 lbs"
    LARGE_BREED = "Large Breed - 50-100 lbs"
    GIANT_BREED = "Giant Breed - 100+ lbs"


class WeightRange(Enum):
    UP_TO_10_LBS = "Up to 10 lbs"
    FROM_10_TO_20_LBS = "10-20 lbs"
    FROM_20_TO_50_LBS = "20-50 lbs"
    FROM_50_TO_100_LBS = "50-100 lbs"
    OVER_100_LBS = "Over 100 lbs"


class Pet(models.Model):

  """
  Pet model to store information about pets belonging to clients.
  """
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

  # Client - Foreign Key
  client = models.ForeignKey("Client", on_delete=models.CASCADE)

  # Name
  name = models.CharField(max_length=255)

  # DOB - I'd like to system to record the date of birth and then use it to calculate real time age
  dob = models.DateField()

  # Size - Drop down list with size options
  size = models.CharField(max_length=32, choices=[(size.name, size.value) for size in PetSize])

  # Weight - Drop down list with weight ranges (this is typically only needed for dogs). Select one.
  weight = models.CharField(max_length=32, choices=[(size.name, size.value) for size in WeightRange])

  # Usual Food Brands - Free form
  usual_food_brands = models.TextField()

  # Allergies - Yes/No
  allergies = models.BooleanField()

  # Allergies Type - Drop down list with an "other" option that is free form text. Select all that apply
  allergy_types = models.ManyToManyField("AllergyType")

  # Pictures - For no reason other than I think it would be fun to have their client dashboard have pics of their pets for the profiles
  pictures = models.ImageField(upload_to="pet_pictures/", null=True, blank=True)

  def __str__(self):
    return self.name
