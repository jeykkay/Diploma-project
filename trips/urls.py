from django.urls import path
from trips.views import CarListView, TripListView

urlpatterns = [
    path('cars/', CarListView.as_view(), name='cars'),
    path('trips/', TripListView.as_view(), name='trips')

]
