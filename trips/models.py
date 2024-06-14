from django.db import models
from users.models import Passenger, Driver


class Car(models.Model):
    brand = models.CharField(max_length=255, blank=False, null=False)
    model = models.CharField(max_length=255, blank=False, null=False)
    year = models.PositiveIntegerField(blank=False, null=False)
    color = models.CharField(max_length=255, blank=False, null=False)
    num_car = models.PositiveIntegerField(unique=True, blank=False, null=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand}-{self.model}: {self.num_car}"

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"


class Trip(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=False)
    start_time = models.TimeField(blank=False, null=False)
    end_time = models.TimeField(blank=False, null=False)
    destination = models.CharField(max_length=255, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)

    def __str__(self):
        return f"{self.driver}-{self.car}: started order {self.date} at {self.start_time}\nPrice: {self.price}"

    class Meta:
        verbose_name = "Trip"
        verbose_name_plural = "Trips"


class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=False)
    time = models.TimeField(blank=False, null=False)

    def __str__(self):
        return f"The car {self.car} is reserved {self.date} at {self.time}"

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"


class Rating(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    rating = models.FloatField(blank=False, null=False)

    def __str__(self):
        return f"{self.passenger.name} rated the {self.driver.name}: {self.rating}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"


class Comment(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.passenger.name} commented on {self.trip} at {self.created_at}\n{self.text}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
