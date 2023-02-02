from nextcord import Interaction, SlashOption, SelectOption, Embed
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

    
    @bot.slash_command(name="carrierlist", description="Get a list of all Squadron Carriers", guild_ids=[TESTING_GUILD_ID]) #Maybe push to Admin only! (ID and Name of Carrier visible)
    async def carrierlist(interaction: Interaction):
        # get all carrier names
        carrierNames = getAllCarrierNames()
        embed = Embed(title="All Squadron Carriers", description="Here is a list of all Squadron Carriers", color=0xffb400)
        
        for carrier in carrierNames:
            embed.add_field(name=carrierNames[carrier], value=f"ID: {carrier}", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)


