from nextcord import Interaction, SlashOption, Role, Permissions, Member

from helpfunctions import formatCarrierName
from caching import getCarrierIdByName, getCarrierObjectByID

def initAdminCommands(bot, args_dict):

    TESTING_GUILD_ID = args_dict["TESTING_GUILD_ID"]

    @bot.slash_command(name="registerrole", description="Registers a Role that can use the Bot", guild_ids=[TESTING_GUILD_ID], default_member_permissions=Permissions(administrator=True))
    async def registerRole(interaction: Interaction, roles: Role = SlashOption(name="roles", description="The Role that should be registered", required=True)):
        await interaction.response.send_message("Role registered") 

    @bot.slash_command(name="setcarrierownerdiscordid", description="Sets the owner discord id of a specified Carrier", guild_ids=[TESTING_GUILD_ID], default_member_permissions=Permissions(administrator=True))
    async def setCarrierOwnerDiscordID(interaction: Interaction, captain: Member = SlashOption(name="user", description="The Owner of the Carrier", required=True), carrierName: str = SlashOption(name="carrier_name", description="The Carrier that get's a new Owner")):
        carrierName = formatCarrierName(carrierName)
        carrierid = getCarrierIdByName(carrierName)
        if carrierid == None:
            await interaction.response.send_message("Carrier not found!", ephemeral=True)
            return
        
        carrier = getCarrierObjectByID(carrierid)
        carrier.setCarrierOwnerDiscordID(captain.id)
        await interaction.response.send_message(f"Carrier Owner for {carrierName} set!", ephemeral=True)
