from caching import getAllCarrierNamesAsList
from difflib import get_close_matches

def formatCarrierName(carrierName):
    if not carrierName.startswith("RST "):
        carrierName = "RST " + carrierName
    carrierNames = getAllCarrierNamesAsList()
    if carrierName in carrierNames:
        return carrierName
    matches = get_close_matches(carrierName, carrierNames, n=1, cutoff=0.8)
    if len(matches) > 0:
        carrierName = matches[0]
        return carrierName
    return None