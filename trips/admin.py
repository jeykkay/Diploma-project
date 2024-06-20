from django.contrib import admin
from trips.models import Car, Trip, Booking, Rating, Comment


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'color', 'num_car', )


@admin.register(Trip)
class TripsAdmin(admin.ModelAdmin):
    list_display = ('driver', 'car', 'date', 'start_time', 'end_time', 'destination', 'price', )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('driver', 'car', 'date', 'time')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('driver', 'rating', )


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('passenger', 'driver', 'text', 'created_at', )
