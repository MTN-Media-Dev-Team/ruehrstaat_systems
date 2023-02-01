import json, os, requests, logging

from .service import Service as CarrierService

CARRIER_SERVICES = {}

# request list of services from api
def getServices():
    url = 'https://api.ruehrstaat.de/api/v1/getAllServices'
    headers = {'Authorization': 'Bearer ' + os.getenv("READ_API_KEY")}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        services = json.loads(response.text)
        for service in services:
            CARRIER_SERVICES[service["name"]] = CarrierService(service["name"], service["label"], service["description"], bool(service["odyssey"]))
    else:
        return None
getServices()

class Carrier:
    def __init__(self, carrier_id):
        self.id = carrier_id

    def setCarrierData(self, carrier_data):
        self.name = carrier_data["name"]
        self.callsign = carrier_data["callsign"]
        self.current_location = carrier_data["current_location"]
        self.previous_location = carrier_data["previous_location"]
        self.dockingAccess = carrier_data["dockingAccess"]
        self.owner = carrier_data["owner"]
        
        # go through carrier_data services, search for them in CARRIER_SERVICES and add them to self.services
        self.services = []
        for service in carrier_data["services"]:
            if service["name"] in CARRIER_SERVICES:
                self.services.append(CARRIER_SERVICES[service["name"]])
        
logging.debug(CARRIER_SERVICES)
