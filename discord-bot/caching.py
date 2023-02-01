from classes import Carrier
import requests, os, time, json

cached_carriers = {}

def __getCarrierInfo(carrierID):
    url = 'https://api.ruehrstaat.de/api/v1/carrier?id=' + str(carrierID)
    headers = {'Authorization': 'Bearer ' + os.getenv("READ_API_KEY")}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        carrier_data = json.loads(response.content)["carrier"]
        carrier = Carrier(carrierID)
        carrier.setCarrierData(carrier_data)
        cached_carriers[carrierID] = carrier
        return carrier
    else:
        return None

def getCarrierObjectByID(carrierID):
    if carrierID in cached_carriers:
        # check if carrier.last_update is older than 15 minutes
        if cached_carriers[carrierID].last_update < time.time() - 900:
            # if older than 15 minutes, update carrier
            return __getCarrierInfo(carrierID)
        return cached_carriers[carrierID]
    else:
        return __getCarrierInfo(carrierID)

def getCarrierObjectByName(carrierName):
    for carrier in cached_carriers:
        if carrier.name == carrierName:
            return carrier
    return None
