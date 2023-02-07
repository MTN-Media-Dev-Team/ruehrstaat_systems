from rest_framework import serializers

from carriers.models import Carrier
from carriers.models import CarrierService

class CarrierServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarrierService
        fields = ('name', 'label', 'description', 'odyssey')

class CarrierSerializer(serializers.ModelSerializer):
    services = CarrierServicesSerializer(many=True, read_only=True)
    dockingAccess = serializers.ChoiceField(choices=Carrier.DOCKING_ACCESS_CHOICES, default='all', source='get_dockingAccess_display')
    category = serializers.ChoiceField(choices=Carrier.CARRIER_CATEGORY_CHOICES, default='other', source='get_category_display')
    class Meta:
        model = Carrier
        fields = ['id', 'name', 'callsign', 'currentLocation', 'previousLocation', 'dockingAccess', 'services', 'owner', 'ownerDiscordID', 'imageURL', 'category']

