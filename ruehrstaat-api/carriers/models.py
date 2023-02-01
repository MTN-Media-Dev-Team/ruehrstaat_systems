from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

# Create your models here.

class CarrierService(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    label = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    # mark as odyssey only
    odyssey = models.BooleanField(default=False)

    def __str__(self):
        return self.label


class Carrier(models.Model):
    # each carrier has a unique id provided when creating a carrier and is used as primary key
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    callsign = models.CharField(max_length=255, unique=True, null=False, blank=False)
    currentLocation = models.CharField(max_length=255, null=False, blank=False)
    previousLocation = models.CharField(max_length=255, null=True, blank=True)
    services = models.ManyToManyField(CarrierService)
    
    # docking access can be ONE of the following: all/none/friends/squadron/squadronfriends and ONLY allow one of these values
    DOCKING_ACCESS_CHOICES = [
        ('all', 'All'),
        ('none', 'None'),
        ('friends', 'Friends'),
        ('squadron', 'Squadron'),
        ('squadronfriends', 'Squadron & Friends'),
    ]
    dockingAccess = models.CharField(max_length=255, choices=DOCKING_ACCESS_CHOICES, default='all')

    owner = models.CharField(max_length=255, null=False, blank=False)

    imageURL = models.URLField(max_length=255, null=True, blank=True)
    isFlagship = models.BooleanField(default=False)

    def __str__(self):
        return self.name