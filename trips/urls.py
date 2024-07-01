from django.urls import path
from rest_framework.routers import DefaultRouter

from trips.views import (CarViewSet, TripViewSet,
                         BookingAPIView)


router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')
router.register(r'trips', TripViewSet, basename='trips')

urlpatterns = [
    path('create-booking/', BookingAPIView.as_view(), name='create-booking'),
]

urlpatterns += router.urls
