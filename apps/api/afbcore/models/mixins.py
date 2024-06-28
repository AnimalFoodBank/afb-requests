from django.db import models


class HasDetailsMixin(models.Model):
    """
    A mixin for models that have a details field.

    Fields:
        - details: JSONField, blank=True, default=dict
    """

    details = models.JSONField(blank=True, default=dict)

    class Meta:
        abstract = True


class PhysicalLocationMixin(models.Model):
    """
    Represents a single, IRL physical location.

    This is used for branches, but could also be used for other things like
    drop off locations, etc.
    """

    # Location Name / Area nameie Winnipeg, MB; Medicine Hat, AB etc.
    location_name = models.CharField(
        max_length=255, help_text="ie Winnipeg, MB;  Medicine Hat, AB etc."
    )

    # Street address
    address_line1 = models.CharField(max_length=255, null=True, blank=True)
    address_line2 = models.CharField(max_length=255, null=True, blank=True)

    # City
    city = models.CharField(max_length=255, null=True, blank=True)

    # State or province
    state_or_province = models.CharField(max_length=255, null=True, blank=True)

    # Postal code or ZIP code
    postal_code = models.CharField(max_length=255, null=True, blank=True)

    # Country
    country = models.CharField(max_length=255, null=True, blank=True)

    # External ID.
    # The unique idenifier from a Canada Post API request. This is used to
    # indicate the address has been validated. However, street names/numbers
    # postal codes can be modified by Canada Post, so this location may have
    # been valid in the past but this is not the source of truth for the address.
    ext_id = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True
