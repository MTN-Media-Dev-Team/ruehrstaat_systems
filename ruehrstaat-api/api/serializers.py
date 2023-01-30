from rest_framework import serializers

from carriers.models import Carrier
from carriers.models import CarrierService

class CarrierServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarrierService
        fields = ('name', 'description', 'odyssey')

class CarrierSerializer(serializers.ModelSerializer):
    services = CarrierServicesSerializer(many=True, read_only=True)

    class Meta:
        model = Carrier
        fields = ['id', 'name', 'callsign', 'currentLocation', 'previousLocation', 'services', 'dockingAccess', 'owner']

