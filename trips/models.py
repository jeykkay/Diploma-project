from django.db import models
from users.models import CustomUser, Driver


class Car(models.Model):
    brand = models.CharField(max_length=255, blank=False, null=False, verbose_name='Марка автомобиля')
    model = models.CharField(max_length=255, blank=False, null=False, verbose_name='Модель автомобиля')
    year = models.PositiveIntegerField(blank=False, null=False, verbose_name='Год')
    color = models.CharField(max_length=255, blank=False, null=False, verbose_name='Цвет')
    num_car = models.PositiveIntegerField(unique=True, blank=False, null=False, verbose_name='Гос номер автомобиля')
    is_available = models.BooleanField(default=True, verbose_name='Статус')

    def __str__(self):
        return f"{self.brand}-{self.model}: {self.num_car}"

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"


class Trip(models.Model):
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, related_name="trip_as_driver")
    passenger = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="trip_as_passenger")
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=False, verbose_name='Дата поездки')
    start_time = models.TimeField(blank=False, null=False, verbose_name='Дата начала поездки')
    end_time = models.TimeField(blank=False, null=False, verbose_name='Дата окончания поездки')
    destination = models.CharField(max_length=255, blank=False, null=False, verbose_name='Место назначения')
    price = models.FloatField(blank=False, null=False, verbose_name='Цена')

    def __str__(self):
        return f"{self.driver}-{self.car}: started order {self.date} at {self.start_time}\nPrice: {self.price}"

    class Meta:
        verbose_name = "Поездка"
        verbose_name_plural = "Поездки"


class Booking(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name="booking_as_car")
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, related_name="booking_as_driver")
    passenger = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="booking_as_passenger")
    date = models.DateField(blank=False, null=False, verbose_name='Дата брони')
    time = models.TimeField(blank=False, null=False, verbose_name='Время брони')

    def __str__(self):
        return f"The car {self.car} is reserved {self.date} at {self.time}"

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"


class Rating(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    rating = models.FloatField(blank=False, null=False, verbose_name='Рейтинг')

    def __str__(self):
        return f"{self.driver}'s rating is {self.rating}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Comment(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='comments')
    passenger = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.passenger.name} commented on {self.trip} at {self.created_at}\n{self.text}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
