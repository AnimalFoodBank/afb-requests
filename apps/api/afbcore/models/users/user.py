import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserManager(models.Manager):
    pass


class UserQuerySet(models.QuerySet):
    pass


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    objects = UserManager.from_queryset(UserQuerySet)()
