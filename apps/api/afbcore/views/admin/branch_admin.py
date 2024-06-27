from django.contrib import admin
from django.utils.html import format_html

from ...models import Branch


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = (
        "display_name",
        "location_name",
        "city",
        "state_or_province",
        "country",
        "operational",
        "hidden",
    )
    list_filter = (
        "operational",
        "hidden",
        "spay_neuter_requirement",
        "delivery_type",
    )
    search_fields = (
        "display_name",
        "location_name",
        "city",
        "state_or_province",
        "country",
    )
    readonly_fields = ("id",)

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "id",
                    "display_name",
                    "blurb",
                    "blurb_image",
                    "operational",
                    "hidden",
                )
            },
        ),
        (
            "Location",
            {
                "fields": (
                    "location_name",
                    "address_line1",
                    "address_line2",
                    "city",
                    "state_or_province",
                    "postal_code",
                    "country",
                    "ext_id",
                    "latitude",
                    "longitude",
                )
            },
        ),
        (
            "Delivery Information",
            {
                "fields": (
                    "delivery_regions",
                    "pickup_locations",
                    "delivery_type",
                    "delivery_pickup_details",
                    "delivery_radius",
                    "delivery_deadline_days",
                )
            },
        ),
        (
            "Branch Policies",
            {
                "fields": (
                    "frequency_of_requests",
                    "spay_neuter_requirement",
                    "pets_per_household_max",
                )
            },
        ),
    )

    def blurb_image_preview(self, obj):
        if obj.blurb_image:
            return format_html(
                '<img src="{}" width="100" height="100" />', obj.blurb_image.url
            )
        return "No Image"

    blurb_image_preview.short_description = "Blurb Image Preview"

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ("id",)
        return self.readonly_fields

    filter_horizontal = ("delivery_regions",)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "delivery_regions":
            kwargs["widget"] = admin.widgets.FilteredSelectMultiple(
                "Delivery Regions", is_stacked=False
            )
        return super().formfield_for_manytomany(db_field, request, **kwargs)
