from nextcord import Interaction, SelectOption
from nextcord.ui import Select, View
from caching import getAllCarrierNames




def initMarketCommands(bot, args_dict):
    TESTING_GUILD_ID = args_dict["TESTING_GUILD_ID"]
    @bot.slash_command(name="setmarketembed", description="Sets the embed for the market", guild_ids=[TESTING_GUILD_ID])
    async def setmarketembed(interaction: Interaction):
        carrierNames = getAllCarrierNames()
        selectCarrier = Select(placeholder="Select a Carrier", options=[SelectOption(label=carrierNames[carrier], value=carrier) for carrier in carrierNames])
        await interaction.response.send_message("Placeholder")
