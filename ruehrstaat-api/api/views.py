from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from carriers.models import Carrier
from .models import ApiKey
from .auth import HasAPIKey, checkForReadAccessAll, checkForReadAccess, checkForWriteAccessAll, checkForWriteAccess
from .serializers import CarrierSerializer

# get all registered carriers

class getAllCarriers(APIView):

    permission_classes = [HasAPIKey]
    # get all carriers
    def get(self, request):
        access_carrier_ids = checkForReadAccessAll(request)
        carriers = Carrier.objects.all()
        # create a list of carriers that are allowed to be accessed
        if access_carrier_ids:
            carriers = carriers.filter(id__in=access_carrier_ids)
        serializer = CarrierSerializer(carriers, many=True)
        return JsonResponse({'carriers': serializer.data}, safe=False)



class carrier(APIView):

    permission_classes = [HasAPIKey]

    def get(self, request):
        carrier_id = request.GET.get('id')
        if not carrier_id:
            return Response({'error': 'No carrier id provided'}, status=status.HTTP_400_BAD_REQUEST)

        if not Carrier.objects.filter(id=carrier_id):
            return Response({'error': 'Invalid carrier id provided'}, status=status.HTTP_400_BAD_REQUEST)
        carrier = Carrier.objects.get(id=carrier_id)
        if not checkForReadAccess(request, carrier_id):
            return Response({'error': 'Carrier not allowed'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = CarrierSerializer(carrier)
        return JsonResponse({'carrier': serializer.data}, safe=False)

    def put(self, request):
        carrier_id = request.data.get('id')
        if carrier_id:
            if not Carrier.objects.filter(id=carrier_id):
                return Response({'error': 'Invalid carrier id provided, to create a carrier please use POST request'}, status=status.HTTP_400_BAD_REQUEST)
            carrier = Carrier.objects.get(id=carrier_id)
            # check for access to carrier
            if not checkForWriteAccess(request, carrier_id):
                return Response({'error': 'Carrier not allowed'}, status=status.HTTP_401_UNAUTHORIZED)

            # update carrier with new values from post form, if fields empty use old values
            if request.data.get('name'):
                carrier.name = request.data.get('name')
            if request.data.get('callsign'):
                carrier.callsign = request.data.get('callsign')
            if request.data.get('currentLocation'):
                carrier.currentLocation = request.data.get('currentLocation')
            if request.data.get('nextLocation'):
                carrier.nextLocation = request.data.get('nextLocation')
            if request.data.get('nextDestination'):
                carrier.nextDestination = request.data.get('nextDestination')
            if request.data.get('nextDestinationTime'):
                carrier.nextDestinationTime = request.data.get('nextDestinationTime')
            if request.data.get('departureTime'):
                carrier.departureTime = request.data.get('departureTime')
            if request.data.get('dockingAccess'):
                carrier.dockingAccess = request.data.get('dockingAccess')
            if request.data.get('owner'):
                carrier.owner = request.data.get('owner')
            carrier.save()
            serializer = CarrierSerializer(carrier)
            return Response({'carrier': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        if request.data.get('id'):
            return Response({'error': 'Use PUT request to edit carrier'}, status=status.HTTP_400_BAD_REQUEST)
        if not checkForWriteAccess(request, None):
            return Response({'error': 'Not allowed to create new carriers'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = CarrierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'carrier': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        carrier_id = request.GET.get('id')
        if not carrier_id:
            return Response({'error': 'No carrier id provided'}, status=status.HTTP_400_BAD_REQUEST)
        if not Carrier.objects.filter(id=carrier_id):
            return Response({'error': 'Invalid carrier id provided'}, status=status.HTTP_400_BAD_REQUEST)
        carrier = Carrier.objects.get(id=carrier_id)
        if not checkForWriteAccess(request, carrier_id):
            return Response({'error': 'Carrier not allowed'}, status=status.HTTP_401_UNAUTHORIZED)
        carrier.delete()
        return Response({'success': 'carrier successfully deleted'}, status=status.HTTP_204_NO_CONTENT)
            

                
                




