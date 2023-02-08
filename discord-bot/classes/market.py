from nextcord.ui import View
from nextcord import Embed
from datetime import datetime as dt

class Market:
    def __init__(self, carrier, marketitemname, marketitemamount, marketitemvalue, station, system, trade_type, opened_by, owner):
        self.view = View()
        self.embed = Embed(title="TRADE ALERT - Market", timestamp=dt.utcnow())
        self.embed.add_field(name= "Carrier:", value=f"{carrier.name} - {carrier.callsign}", inline=False)
        self.embed.add_field(name="Owner:", value=owner, inline=True)
        self.embed.add_field(name="Opened by:", value=opened_by, inline=True)
        self.embed.add_field(name="Item:", value=marketitemname, inline=False)
        self.embed.add_field(name="Amount:", value=marketitemamount, inline=True)
        if trade_type == "Buy":
            self.embed.add_field(name="Carrier buys for:  ", value=marketitemvalue, inline=True)
        else:
            self.embed.add_field(name="Carrier sells for:  ", value=marketitemvalue, inline=True)
        self.embed.add_field(name="Station", value=station, inline=True)
        self.embed.add_field(name="System", value=system, inline=True)
        self.embed.set_image(url=carrier.imageURL)
        self.embed.colour = 0xffb400
        self.embed.set_footer(text=f'powered by Ruehrstaat API')
        
