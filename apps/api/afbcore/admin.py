from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from drfpasswordless.admin import CallbackInline
from drfpasswordless.models import CallbackToken

from .models import (
    Branch,
    Delivery,
    DeliveryRegion,
    FoodAvailable,
    FoodRequest,
    Pet,
    Profile,
    User,
)
from .views.admin.branch_admin import BranchAdmin


class UserAdmin(BaseUserAdmin):
    inlines = [CallbackInline]
    list_display = ("username", "email", "name", "is_staff", "callbacktoken")

    def callbacktoken(self, obj):
        tokens = obj.callbacktoken_set.active()
        return ", ".join([token.key for token in tokens])

    callbacktoken.short_description = "Active Magic Codes"


class AuthorAdmin(admin.ModelAdmin):
    fields = ["name", "title"]


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
# admin.site.register(Branch, BranchAdmin)
admin.site.register(FoodRequest)
admin.site.register(Delivery)
admin.site.register(DeliveryRegion)
admin.site.register(FoodAvailable)
admin.site.register(Pet)
admin.site.register(CallbackToken)
