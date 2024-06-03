from django.db import models
from model_utils.managers import QueryManagerMixin, SoftDeletableManagerMixin
from model_utils.models import (  # StatusModel,
    SoftDeletableModel,
    TimeStampedModel,
    UUIDModel,
)

"""
    Usage:

    from .base import BaseAbstractModel

    class MyModel(BaseAbstractModel):
        # fields go here
        pass
"""


class BaseAbstractModelManager(
    SoftDeletableManagerMixin, QueryManagerMixin, models.Manager
):
    """A common base class for core model managers"""


class BaseAbstractQuerySet(models.QuerySet):
    """A common base class for core model querysets"""


class BaseAbstractModel(UUIDModel, SoftDeletableModel, TimeStampedModel):
    """A common base class for core models

    Fields inherited from BaseAbstractModel:
        - id: UUIDField, primary key
        - created: DateTimeField, auto_now_add=True
        - updated: DateTimeField, auto_now=True
        - is_removed: BooleanField, default=False
    """

    class Meta:
        abstract = True

    objects = BaseAbstractModelManager()


class HasDetails(models.Model):
    """
    A mixin for models that have a details field.

    Fields:
        - details: JSONField, blank=True, default=dict
    """

    details = models.JSONField(blank=True, default=dict)

    class Meta:
        abstract = True
