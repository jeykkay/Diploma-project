from django.urls import path

from trips.views import CarListView, TripListView, CarDetailView

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car_list'),
    path('cars/<int:car_id>/', CarDetailView.as_view(), name='car'),

    path('trips/', TripListView.as_view(), name='trip_list')
]
