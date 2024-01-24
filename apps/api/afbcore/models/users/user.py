"""
    AFB Core API User Model

    NOTE: We define a custom manager for this model in order to provide
    create_user and create_superuser methods. We could have implemented
    these methods in the model itself, but it's better to keep the model
    as simple as possible. Otherwise, the rest of the functionality
    comes from Django's built-in UserManager.

    NOTE 2: However, that means we need to be careful wuth regards to soft
    detletes. If we use the delete method provided by the default manager,
    it will delete the object from the database. Instead, we should only
    ever delete Users using the user.delete() method.

"""
import logging

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import UserManager as DefaultUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel, UUIDModel

logger = logging.getLogger(__name__)


class UserManager(BaseUserManager):
    def is_a_truly_unique(self, field_name, value):
        """
        Check the given value against the database.

        Used by VueformUniqueValidatorView for checking uniqueness
        of email field.
        """
        logger.debug(f"UserManager.is_a_truly_unique - {field_name}: {value}")

        # Fast fail on bad input.
        if value is None or value == "":
            logger.info(f"UserManager.is_a_truly_unique - value is None or empty")
            return False

        # Assume pessimistically that the value is not unique.
        is_unique = False

        try:
            record = User.objects.get(**{field_name: value})
            logger.info(f"UserManager.is_a_truly_unique - record: {record.pk}")

        except User.DoesNotExist:
            logger.info(f"UserManager.is_a_truly_unique - DoesNotExist")
            is_unique = True

        return is_unique

    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(UUIDModel, TimeStampedModel, AbstractUser):
    """
    A custom user model that extends Django's built-in AbstractUser model.

    Fields inherited from AbstractUser:
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

    # Use custom manager.
    objects = UserManager()

    USERNAME_FIELD = "email"

    # From the docs:
    #
    # REQUIRED_FIELDS must contain all required fields on your user model,
    # but should not contain the USERNAME_FIELD or password as these
    # fields will always be prompted for.
    REQUIRED_FIELDS = [
        "name",
    ]

    # Override the email field from AbstractUser to make it unique.
    email = models.EmailField(_("email address"), unique=True)

    # Add a single name field which we'll use instead of the default
    # first_name and last_name fields.
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

    # Remove the first_name and last_name fields from AbstractUser.
    first_name = None
    last_name = None
