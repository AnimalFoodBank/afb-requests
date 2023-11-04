import uuid
from django.db import models
from model_utils import Choices
from model_utils.managers import SoftDeletableManagerMixin, QueryManagerMixin
from model_utils.models import (
    TimeStampedModel,
    SoftDeletableModel,
    # StatusModel,
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
    """A common base class for all major core managers"""


class BaseAbstractQuerySet(models.QuerySet):
    """A common base class for all major core querysets"""


class BaseAbstractModel(UUIDModel, SoftDeletableModel, TimeStampedModel):
    """A common base class for all major core models

    Fields inherited from BaseAbstractModel:
        - id: UUIDField, primary key
        - created: DateTimeField, auto_now_add=True
        - updated: DateTimeField, auto_now=True
        - is_removed: BooleanField, default=False
    """

    class Meta:
        abstract = True

    objects = BaseAbstractModelManager()
