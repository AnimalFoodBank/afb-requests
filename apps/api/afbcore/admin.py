from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from drfpasswordless.admin import CallbackInline
from drfpasswordless.models import CallbackToken


from .models import (
    Profile,
    User,
    Role,
    Branch,
    Request,
    Delivery,
    DeliveryRegion,
    FoodAvailable,
    Pet,
)


class UserAdmin(BaseUserAdmin):
    inlines = [CallbackInline]
    list_display = ("username", "email", "name", "is_staff", "callbacktoken")

    def callbacktoken(self, obj):
        tokens = obj.callbacktoken_set.active()
        return ", ".join([token.key for token in tokens])

    callbacktoken.short_description = "Active Magic Codes"


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Role)
admin.site.register(Branch)
admin.site.register(Request)
admin.site.register(Delivery)
admin.site.register(DeliveryRegion)
admin.site.register(FoodAvailable)
admin.site.register(Pet)
admin.site.register(CallbackToken)
