from django.contrib import admin
from users.models import CustomUser, Driver


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    ...


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    ...
