
import uuid
from django.db import models

# Status - Active, On Hold, Banned
STATUS_CHOICES = [
    ('active', 'Active'),
    ('on_hold', 'On Hold'),
    ('banned', 'Banned'),
]

class Client(models.Model):

  """
  Clients could try to scam and create duplicate accounts to circumvent frequency, change pet info, etc.
  We need to do our best to ensure each account is unique.
  """
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

  branch = models.ForeignKey('Branch', on_delete=models.DO_NOTHING)

  # First Name
  first_name = models.CharField(max_length=255)

  # Last Name
  last_name = models.CharField(max_length=255)

  # Email - Unique - don't allow duplicates.
  email = models.EmailField(unique=True)

  # Address - If address is duplicate to another clients, both accounts need to be placed on hold and manually reviewed/approved bc people are scammers.
  # Has to be a validated address (google?) and not permitted to be overwritten. The last amount of free form text entry as possible.
  # You'd be amazed how many clients don't know their postal code and we route by postal code sooooo
  address = models.CharField(max_length=255)

  # Postal/Zip Code - Has to be a validated address (google?) and not permitted to be overwritten. The last amount of free form text entry as possible.
  # You'd be amazed how many clients don't know their postal code and we route by postal code sooooo
  validated_postal_code = models.CharField(max_length=20, null=True)

  # Country - I don't know if we need this but google addresses populate country too. It may be useful for analytics
  country = models.CharField(max_length=255, blank=True)

  # Phone - Validate format - numbers only
  phone_number = models.CharField(max_length=20)

  # Agree to Terms and Conditions
  agreed_to_terms = models.BooleanField()

  # Agreed on date - Yes/No
  agreed_on_date = models.DateField(null=True, blank=True)


  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

  def __str__(self):
    return f"{self.first_name} {self.last_name}"
