import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserManager(models.Manager):
    pass


class UserQuerySet(models.QuerySet):
    pass


class User(AbstractUser):
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

    Additional fields:
    - id: UUIDField, primary key
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    objects = UserManager.from_queryset(UserQuerySet)()
