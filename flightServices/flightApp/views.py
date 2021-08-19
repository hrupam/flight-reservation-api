from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
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


@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['flightId'])

    passenger = Passenger()

    passenger.firstName = request.data['firstName']
    passenger.middleName = request.data['middleName'] if 'middleName' in request.data else None
    passenger.lastName = request.data['lastName']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']

    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger

    reservation.save()

    serializer = ReservationSerializer(reservation)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


@api_view(['GET'])
def get_passengers(request, flightId):
    flight = Flight.objects.filter(id=flightId).first()

    reservations = Reservation.objects.filter(flight=flight)
    passenger_ids = []
    for res in reservations:
        passenger_ids.append(res.passenger.id)

    passengers = Passenger.objects.filter(id__in=passenger_ids)

    serializer = PassengerSerializer(passengers, many=True)
    return Response(serializer.data)
