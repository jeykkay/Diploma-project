from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from trips.serializer import (CarSerializer, TripSerializer,
                              BookingSerializer)
from trips.models import (Car, Trip,
                          Booking, Rating,
                          Comment)


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (AllowAny, )


class TripViewSet(ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = (AllowAny, )


class BookingAPIView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RatingAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    ...


class CommentAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    ...
