from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from trips.models import Car, Trip
from trips.serializers import CarSerializer, TripSerializer


class CarListView(ListAPIView):
    queryset = Car.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = CarSerializer


class TripListView(ListAPIView):
    queryset = Trip.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = TripSerializer


class BookingApiView(APIView):
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = BookingSerializer
