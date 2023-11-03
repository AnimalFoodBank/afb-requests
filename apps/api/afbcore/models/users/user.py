from django.contrib.auth.models import UserManager as DefaultUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from ..base import BaseAbstractModel


class User(BaseAbstractModel, AbstractUser):
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

    Fields inherited from BaseAbstractModel:
    - id: UUIDField, primary key
    - created: DateTimeField, auto_now_add=True
    - updated: DateTimeField, auto_now=True
    - is_removed: BooleanField, default=False
    """

    # NOTE: We don't need to define a custom manager for this model because
    # Django's built-in UserManager already provides the functionality we need.
    # It's also a bit of a pain to implement properly.

    # NOTE 2: However, that means we need to be careful wuth regards to soft
    # detletes. If we use the delete method provided by the default manager,
    # it will delete the object from the database. Instead, we should only
    # ever delete Users using the user.delete() method.


q
