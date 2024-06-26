from django.urls import path
from rest_framework.routers import DefaultRouter

from trips.views import (CarViewSet, TripViewSet)


router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')
router.register(r'trips', TripViewSet, basename='trips')

urlpatterns = [

]

urlpatterns += router.urls
