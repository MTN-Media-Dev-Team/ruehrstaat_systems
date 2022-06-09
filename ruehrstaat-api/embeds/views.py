from django.shortcuts import render

from carriers.models import Carrier, CarrierService
from carriers.info import getCarrierInfo

from rest_framework import status
from rest_framework.response import Response

def seeCarrier(request, carrier_id):
    #get the carrier info as json data
    carrier = getCarrierInfo(carrier_id)
    if not carrier:
        return render(request, 'embeds/404.html')
    return render(request, 'embeds/carrier.html', {'carrier': carrier})

    


