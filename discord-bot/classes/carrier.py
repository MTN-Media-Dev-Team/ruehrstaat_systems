import json, os, requests, logging, time

from .service import Service as CarrierService

CARRIER_SERVICES = {}

# request list of services from api
def getServices():
    url = 'https://api.ruehrstaat.de/api/v1/getAllServices'
    headers = {'Authorization': 'Bearer ' + os.getenv("READ_API_KEY")}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        services = json.loads(response.content)["services"]
        for service in services:
            CARRIER_SERVICES[service["name"]] = CarrierService(service["name"], service["label"], service["description"], bool(service["odyssey"]))
            logging.debug("Added Service: " + service["name"])
    else:
        return None
getServices()

class Carrier:
    def __init__(self, carrier_id):
        self.id = carrier_id
        self.name = None
        self.callsign = None
        self.current_location = None
        self.previous_location = None
        self.dockingAccess = None
        self.owner = None
        self.services = []
        self.last_update = time.time()
        self.imageURL = None
        self.isFlagship = False

    def setCarrierData(self, carrier_data):
        self.name = carrier_data["name"]
        self.callsign = carrier_data["callsign"]
        self.currentLocation = carrier_data["currentLocation"]
        self.previousLocation = carrier_data["previousLocation"]
        self.dockingAccess = carrier_data["dockingAccess"]
        self.owner = carrier_data["owner"]
        self.imageURL = carrier_data["imageURL"]
        self.isFlagship = bool(carrier_data["isFlagship"])

        # save current timestamp as last update
        self.last_update = time.time()
        
        # go through carrier_data services, search for them in CARRIER_SERVICES and add them to self.services
        self.services = []
        for service in carrier_data["services"]:
            if service["name"] in CARRIER_SERVICES:
                self.services.append(CARRIER_SERVICES[service["name"]])
    
