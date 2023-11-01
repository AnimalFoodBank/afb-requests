import uuid

from django.db import models

from .base_profile import BaseProfile


class Manager(BaseProfile):
    """ """

    role_level = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


"""
GitHub Copilot: Here are all the arguments that can be used with Django's `ManyToManyField`:

- `to`: The model to which the relationship is defined. This can be a string containing the name of the model, or the model class itself.
- `related_name`: The name to use for the reverse relation from the related object back to this one. This is used to access the related objects from the other side of the relationship.
- `related_query_name`: The name to use for the reverse relation from the related object back to this one when performing queries. This is used to filter the related objects from the other side of the relationship.
- `limit_choices_to`: A dictionary of lookup arguments to use when limiting the available choices for the relationship.
- `symmetrical`: A boolean indicating whether the relationship is symmetrical. This is used when the relationship is defined on both sides of the model.
- `through`: The intermediate model to use for the relationship. This is used when you need to add extra fields to the relationship.
- `through_fields`: A tuple of field names that specify the fields on the intermediate model that should be used for the relationship.
- `db_table`: The name of the database table to use for the relationship.
- `db_constraint`: A boolean indicating whether to create a database constraint for the relationship.
- `swappable`: A boolean indicating whether the relationship can be swapped out with another model.
- `blank`: A boolean indicating whether the field is allowed to be blank.
- `null`: A boolean indicating whether the field is allowed to be null.
- `default`: The default value for the field.
- `editable`: A boolean indicating whether the field is editable.
- `help_text`: The help text to display for the field.
- `verbose_name`: The human-readable name to use for the field.
- `validators`: A list of validators to use for the field.
- `error_messages`: A dictionary of error messages to use for the field.
"""
