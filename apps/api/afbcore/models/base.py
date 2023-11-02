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


class BaseAbstractModelManager(
    SoftDeletableManagerMixin, QueryManagerMixin, models.Manager
):
    """A common base class for all major core managers"""


class BaseAbstractQuerySet(models.QuerySet):
    """A common base class for all major core querysets"""


class BaseAbstractModel(UUIDModel, SoftDeletableModel, TimeStampedModel):
    """A common base class for all major core models"""

    class Meta:
        abstract = True

    objects = BaseAbstractModelManager()
