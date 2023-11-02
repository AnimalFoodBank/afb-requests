from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Client, Manager, Volunteer, User

admin.site.register(User, UserAdmin)
admin.site.register(Client)
admin.site.register(Manager)
admin.site.register(Volunteer)


# Register your models here.
