from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
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
