from django.contrib.auth.models import UserManager as DefaultUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from model_utils.models import (
    TimeStampedModel,
    UUIDModel,
)

"""
    AFB Core API User Model

    NOTE: We don't need to define a custom manager for this model because
    Django's built-in UserManager already provides the functionality we need.
    It's also a bit of a pain to implement properly.

    NOTE 2: However, that means we need to be careful wuth regards to soft
    detletes. If we use the delete method provided by the default manager,
    it will delete the object from the database. Instead, we should only
    ever delete Users using the user.delete() method.

"""


class User(UUIDModel, TimeStampedModel, AbstractUser):
    """
    A custom user model that extends Django's built-in AbstractUser model.

    Fields inherited from AbstractUser:
    - username
    - first_name
    - last_name
    - email
    - password
    - groups
    - user_permissions
    - is_staff
    - is_active
    - date_joined
    - last_login

    Fields inherited from UUIDModel, TimeStampedModel:
    - id: UUIDField, primary key
    - created: DateTimeField, auto_now_add=True
    - updated: DateTimeField, auto_now=True
    """

    USERNAME_FIELD = "email"

    # From the docs:
    #
    # REQUIRED_FIELDS must contain all required fields on your user model,
    # but should not contain the USERNAME_FIELD or password as these
    # fields will always be prompted for.
    REQUIRED_FIELDS = [
        "name",
        "terms_agreement",
    ]

    email = models.EmailField(_("email address"), unique=True)

    name = models.CharField(_("name"), max_length=255)

    terms_agreement = models.BooleanField(
        _("terms agreement"),
        default=False,
        help_text=_("Indicates whether the user has agreed to the terms of service."),
    )

    # Override the username field from AbstractUser to allow null values.
    username = models.CharField(
        _("username"), max_length=255, unique=True, null=True, blank=True
    )
