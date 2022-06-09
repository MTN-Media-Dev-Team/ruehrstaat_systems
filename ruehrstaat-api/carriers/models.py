from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

# Create your models here.

class CarrierService(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # mark as odyssey only
    odyssey = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Carrier(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    callsign = models.CharField(max_length=255, unique=True, null=False, blank=False)
    currentLocation = models.CharField(max_length=255, null=False, blank=False)
    nextLocation = models.CharField(max_length=255, null=True, blank=True)
    nextDestination = models.CharField(max_length=255, null=True, blank=True)
    nextDestinationTime = models.DateTimeField(null=True, blank=True)
    departureTime = models.DateTimeField(null=True, blank=True)
    services = models.ManyToManyField(CarrierService)
    dockingAccess = models.BooleanField(default=True, null=False, blank=False)
    owner = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name