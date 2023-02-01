from classes.carrier import Carrier
import requests, os, time, json

from difflib import get_close_matches

cached_carriers = {}

def __getCarrierInfo(carrierID):
    # check if carrier is cached and if yes delete it
    if carrierID in cached_carriers:
        del cached_carriers[carrierID]
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

def __formatCarrierName(carrierName):
    if not carrierName.startswith("RST "):
        carrierName = "RST " + carrierName
    carrierNames = __getAllCarrierNamesAsList()
    if carrierName in carrierNames:
        return carrierName
    matches = get_close_matches(carrierName, __getAllCarrierNamesAsList, n=1, cutoff=0.8)
    if len(matches) > 0:
        carrierName = matches[0]
        return carrierName
    else:
        return "RST Vanguard"

def recacheAllCarriers():
    url = 'https://api.ruehrstaat.de/api/v1/getAllCarriers'
    headers = {'Authorization': 'Bearer ' + os.getenv("READ_API_KEY")}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        all_carrier_data = json.loads(response.content)["carriers"]
        for carrier_data in all_carrier_data:
            carrier = Carrier(carrier_data["id"])
            carrier.setCarrierData(carrier_data)
            cached_carriers[carrier.id] = carrier
    else:
        raise Exception("Could not recache all carriers")

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
    carrierName = __formatCarrierName(carrierName)
    for carrier in cached_carriers:
        if cached_carriers[carrier].name == carrierName:
            # check if carrier.last_update is older than 15 minutes
            if cached_carriers[carrier].last_update < time.time() - 900:
                # if older than 15 minutes, update carrier
                return __getCarrierInfo(carrier)
            return cached_carriers[carrier]
    return None

def getCarrierIdByName(carrierName):
    carrierName = __formatCarrierName(carrierName)
    for carrier in cached_carriers:
        if cached_carriers[carrier].name == carrierName:
            # check if carrier.last_update is older than 15 minutes
            if cached_carriers[carrier].last_update < time.time() - 900:
                # if older than 15 minutes, update carrier
                __getCarrierInfo(carrier)
            return cached_carriers[carrier].id
    return None

def getAllCarrierNames():
    # carrier names as dict with id and name
    carrier_names = {}
    for carrier in cached_carriers:
        carrier_names[carrier] = cached_carriers[carrier].name
    return carrier_names
    
def __getAllCarrierNamesAsList():
    # carrier names as list
    carrier_names = []
    for carrier in cached_carriers:
        carrier_names.append(cached_carriers[carrier].name)
    return carrier_names
