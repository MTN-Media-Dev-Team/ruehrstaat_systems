from nextcord import Interaction, SlashOption, SelectOption
from nextcord.ui import Select, View

from embeds import getCarrierInfoEmbed
from caching import getCarrierIdByName, getAllCarrierNames

def initCarrierCommands(bot, args_dict):
        
    TESTING_GUILD_ID = args_dict["TESTING_GUILD_ID"]
    
    @bot.slash_command(name="carrierinfo", description="Get Information about an specific Squadron Carrier", guild_ids=[TESTING_GUILD_ID])
    async def carrierinfo(interaction: Interaction):
        # get all carrier names
        carrierNames = getAllCarrierNames()
        selectCarrier = Select(placeholder="Select a Carrier", options=[SelectOption(label=carrierNames[carrier], value=carrier) for carrier in carrierNames])

        selectmessage = None

        async def callback(interaction: Interaction):
            # get carrier id
            carrier_id = selectCarrier.values[0]
            if carrier_id == None:
                await interaction.response.send_message("Carrier not found!", ephemeral=True)
                return
            embed, view = getCarrierInfoEmbed(carrier_id)
            await selectmessage.delete()
            await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

        selectCarrier.callback = callback
        view = View()
        view.add_item(selectCarrier)
        selectmessage = await interaction.response.send_message("Select a Carrier", view=view, ephemeral=True)


        
