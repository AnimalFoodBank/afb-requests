import uuid

from django.db import models

# https://django-phonenumber-field.readthedocs.io/en/latest/reference.html#model-field
# https://github.com/google/libphonenumber/blob/master/FALSEHOODS.md
from phonenumber_field.modelfields import PhoneNumberField

from .user import User

# Define default arguments for ManyToManyField
many_to_many_defaults = {
    "related_name": "+",
    "blank": True,
    "symmetrical": False,
}


class BaseProfile(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    # Usually just one, but can be multiple
    branches = models.ManyToManyField("Branch", **many_to_many_defaults)

    # First Name
    first_name = models.CharField(max_length=64)

    # Last Name
    last_name = models.CharField(max_length=64)

    # Email - Unique - don't allow duplicates.
    email = models.EmailField(unique=True)

    # Phone - Validate format - numbers only
    phone_number = PhoneNumberField(
        blank=True,
        null=True,
        region="US",
        max_length=20,
    )

    # We allow free form text entry but store the validated
    # address in the `address` field. These fields should
    # generally be updated together.
    #
    # e.g. A client may enter "123 Main St" and another
    # client may enter "123 Main Street"
    address_verbatim = models.CharField(max_length=255, blank=True)

    # Validated Address
    # i.e. An address from Canada Post or Google Maps
    address = models.CharField(max_length=255, null=True)
