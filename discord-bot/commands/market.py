from nextcord import Interaction, SlashOption
from nextcord.ui import Select, View
from caching import getCarrierObjectByName, getAllMarketNames




def initMarketCommands(bot, args_dict):
    TESTING_GUILD_ID = args_dict["TESTING_GUILD_ID"]
    @bot.slash_command(name="newtrade", description="Sets the embed for the market", guild_ids=[TESTING_GUILD_ID])
    async def newtrade(interaction: Interaction, carriername: str = SlashOption(name="carriername", description="Carrier Selection"), 
    marketitem: str = SlashOption(name="commodity", description="Commodities Selection"), marketitemvalue: int = SlashOption(name="value", description="Value of the Commodity"), marketitemamount: int = SlashOption(name="amount", description="Amount of the Commodity")):
        carriername = getCarrierObjectByName(carriername)
        marketitemname = getAllMarketNames() # TODO: implement Command to get all market names
        await interaction.response.send_message("Placeholder", ephemeral=True)
