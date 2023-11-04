from django.db import models
from ..base import BaseAbstractModel, BaseAbstractQuerySet, BaseAbstractModelManager
from django.core.exceptions import ValidationError


class RoleQuerySet(BaseAbstractQuerySet):
    def by_level(self, level):
        return self.filter(level=level)


class RoleManager(BaseAbstractModelManager):
    def by_level(self, level):
        return self.get_queryset().by_level(level)


class Role(BaseAbstractModel):
    """
    A model representing a user role.

    Attributes:
        name (str): The name of the role.
        level (int): The level of the role between 0 and 100. 0 is the lowest
        level and 99 is the highest level.
    """

    objects = RoleManager.from_queryset(RoleQuerySet)()

    name = models.CharField(max_length=50, unique=True, blank=False, null=False)

    level = models.PositiveSmallIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.name:
            raise ValueError("Name cannot be empty")
        super().save(*args, **kwargs)

    def clean(self):
        if not self.name:
            raise ValidationError("Name cannot be empty")

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name
