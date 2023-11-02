from django.db import models


class RoleQuerySet(models.QuerySet):
    def by_level(self, level):
        return self.filter(level=level)


class RoleManager(models.Manager):
    def get_queryset(self):
        return RoleQuerySet(self.model, using=self._db)

    def by_level(self, level):
        return self.get_queryset().by_level(level)


class Role(models.Model):
    """
    A model representing a user role.

    Attributes:
        name (str): The name of the role.
        level (int): The level of the role between 0 and 100. 0 is the lowest
        level and 99 is the highest level.
    """

    objects = RoleManager.from_queryset(RoleQuerySet)()

    name = models.CharField(max_length=50)
    level = models.SmallIntegerField(default=0)

    def __init__(self, name: str, level: int):
        """
        Initializes a new instance of the Role class.

        Args:
            name (str): The name of the role.
            level (int): The level of the role.
        """
        self.name = name
        self.level = level

    def __str__(self):
        return self.name
