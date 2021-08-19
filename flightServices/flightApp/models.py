from django.db import models

# Create your models here.


class Flight(models.Model):
    flightNumber = models.CharField(max_length=20, unique=True)
    operatingAirlines = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=20)
    arrivalCity = models.CharField(max_length=20)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()

    def __str__(self) -> str:
        return str(self.flightNumber)


class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20, blank=True)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13)

    def __str__(self) -> str:
        return "{} {}".format(self.firstName, self.lastName)


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
