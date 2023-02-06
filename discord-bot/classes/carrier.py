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
        self.ownerDiscordID = None
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

        if carrier_data["ownerDiscordID"]:
            self.ownerDiscordID = int(carrier_data["ownerDiscordID"])
        self.imageURL = carrier_data["imageURL"]
        self.isFlagship = bool(carrier_data["isFlagship"])

        # save current timestamp as last update
        self.last_update = time.time()
        
        # go through carrier_data services, search for them in CARRIER_SERVICES and add them to self.services
        self.services = []
        for service in carrier_data["services"]:
            if service["name"] in CARRIER_SERVICES:
                self.services.append(CARRIER_SERVICES[service["name"]])

    def setCarrierOwnerDiscordID(self, ownerDiscordID, discord_id):
        self.ownerDiscordID = ownerDiscordID
        # write to api
        url = 'https://api.ruehrstaat.de/api/v1/carrier'
        headers = {'Authorization': 'Bearer ' + os.getenv("WRITE_API_KEY")}
        data = {
            "id": self.id,
            "ownerDiscordID": self.ownerDiscordID,
            "source": "discord",
            "discord_id": discord_id
        }
        response = requests.put(url, headers=headers, data=data)
        if response.status_code == 200:
            logging.debug("Successfully updated carrier ownerDiscordID in API")
        else:
            logging.error("Error updating carrier ownerDiscordID in API")

    def setCarrierLocation(self, location, discord_id):
        self.previousLocation = self.currentLocation
        self.currentLocation = location
        # write to api
        url = 'https://api.ruehrstaat.de/api/v1/carrier'
        headers = {'Authorization': 'Bearer ' + os.getenv("WRITE_API_KEY")}
        data = {
            "id": self.id,
            "currentLocation": self.currentLocation,
            "previousLocation": self.previousLocation,
            "source": "discord",
            "discord_id": discord_id
        }
        response = requests.put(url, headers=headers, data=data)
        if response.status_code == 200:
            logging.debug("Successfully updated carrier location in API")
            return True
        else:
            logging.error("Error updating carrier location in API")
            return False
        

    

    

    
