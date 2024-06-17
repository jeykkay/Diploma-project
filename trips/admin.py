from django.contrib import admin
from trips.models import Car, Trip, Booking, Rating, Comment


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'color', 'num_car', )
    search_fields = ('brand', 'model', 'is_available', )


@admin.register(Trip)
class TripsAdmin(admin.ModelAdmin):
    list_display = ('driver', 'car', 'date', 'start_time', 'end_time', 'destination', 'price', )
    search_fields = ('driver', )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('driver', 'car', 'date', 'time')
    search_fields = ('driver', )


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('driver', 'rating', )
    search_fields = ('driver', )


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('passenger', 'driver', 'text', 'created_at', )
    search_fields = ('driver', )
