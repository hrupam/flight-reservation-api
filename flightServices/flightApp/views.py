from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.


@api_view(['POST'])
def find_flights(request):

    flights = Flight.objects.all()

    if 'departureCity' in request.data:
        flights = flights.filter(departureCity=request.data['departureCity'])

    if 'arrivalCity' in request.data:
        flights = flights.filter(arrivalCity=request.data['arrivalCity'])

    if 'dateOfDeparture' in request.data:
        flights = flights.filter(
            dateOfDeparture=request.data['dateOfDeparture'])

    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
