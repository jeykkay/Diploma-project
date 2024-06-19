from django.contrib import admin
from users.models import CustomUser, Driver


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', )


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', )
