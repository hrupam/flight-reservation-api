from django.conf import settings
from django.db import models
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save

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
    middleName = models.CharField(max_length=20, blank=True, null=True)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13)

    def __str__(self) -> str:
        return "{} {}".format(self.firstName, self.lastName)


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
