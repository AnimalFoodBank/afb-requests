from django.contrib import admin

from .models import Branch


class BranchAdmin(admin.ModelAdmin):
    list_display = [
        "display_name",
        "city",
        "province_state",
    ]  # Customize as needed
    # No need to specify read_only_fields unless you want some fields to be read-only in the admin


admin.site.register(Branch, BranchAdmin)
