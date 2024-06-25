from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from trips.serializer import (CarSerializer, TripSerializer,
                              BookingSerializer)
from trips.models import (Car, Trip,
                          Booking)


class CarListView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (AllowAny, )


class CarDetailView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, car_id):
        queryset = Car.objects.filter(id=car_id)
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data)


class TripListView(ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = (AllowAny, )


class BookingAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = BookingSerializer
    ...
