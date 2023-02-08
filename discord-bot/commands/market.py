from nextcord import Interaction, SlashOption, SelectOption
from nextcord.ui import Select, View
from caching import getCarrierObjectByName, getAllMarketNames
from embeds import getMarketEmbed




def initMarketCommands(bot, args_dict):
    
    TESTING_GUILD_ID = args_dict["TESTING_GUILD_ID"]

    @bot.slash_command(name="newtrade", description="Sets the embed for the market", guild_ids=[TESTING_GUILD_ID])
    async def newtrade(interaction: Interaction, carrier: str = SlashOption(name="carriername", description="Carrier Selection"), 
    marketitemname: str = SlashOption(name="commodity", description="Commodities Selection"), marketitemvalue: int = SlashOption(name="value", description="Value of the Commodity"), marketitemamount: int = SlashOption(name="amount", description="Amount of the Commodity"),
    station: str = SlashOption(name="station", description="Station Selection"), system: str = SlashOption(name="system", description="System Selection"), trade_type: str = SlashOption(name="tradetype", description="Trade Type Selection"), required=True):
        carrier = getCarrierObjectByName(carrier)
        marketitemname = getAllMarketNames(marketitemname) # TODO: implement Command to get all market names
        channel_id = "PLACEHOLDER" # TODO: implement Command to get channel id from Database
        trade_type = trade_type
        embed, view = getMarketEmbed(carrier, marketitemname, marketitemamount, marketitemvalue, station, system, trade_type)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True) # ephemeral=True for testing purposes
