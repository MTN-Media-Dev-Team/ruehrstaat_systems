from nextcord import Embed, ButtonStyle
from nextcord.ui import View, Button

from caching import getCarrierObjectByID

def getCarrierInfoEmbed(carrier_id):
    carrier = getCarrierObjectByID(carrier_id)
    embed = Embed(title=f"Carrier Info - {carrier.name} - {carrier.callsign}")
    embed.add_field(name="Current Location", value=carrier.currentLocation, inline=True)
    embed.add_field(name="Docking Access", value=carrier.dockingAccess, inline=True)
    embed.add_field(name="Owner", value=carrier.owner, inline=True)

    # add services
    services = ""
    for service in carrier.services:
        services += f"{service.label}, "
    services = services[:-2]
    embed.add_field(name="Services", value=services, inline=False)
    
    # make embed side color #ffb400
    embed.colour = 0xffb400

    # add image
    embed.set_image(url=carrier.imageURL)

    # set footer
    embed.set_footer(text=f"last updated: {carrier.last_update} - powered by Ruehrstaat API")

    # Add carrier url as button
    view = View()

    if carrier.isFlagship:
        view.add_item(Button(label="Carrier Website", url=f"https://ruehrstaat.de/carrier/{carrier.name.replace(' ', '-')}", style=ButtonStyle.success))
    else:
        view.add_item(Button(label="See all carriers", url=f"https://ruehrstaat.de/carrier/", style=ButtonStyle.success))

    
    return embed, view