from nextcord import Interaction, SlashOption, Role, Permissions, Member

def initAdminCommands(bot, args_dict):

    TESTING_GUILD_ID = args_dict["TESTING_GUILD_ID"]

    @bot.slash_command(name="registerrole", description="Registers a Role that can use the Bot", guild_ids=[TESTING_GUILD_ID], default_member_permissions=Permissions(administrator=True))
    async def registerRole(interaction: Interaction, roles: Role = SlashOption(name="roles", description="The Role that should be registered", required=True)):
        await interaction.response.send_message("Role registered") 

    @bot.slash_command(name="setcarrierowner", description="Sets the owner of a specified Carrier", guild_ids=[TESTING_GUILD_ID], default_member_permissions=Permissions(administrator=True))
    async def setCarrierOwner(interaction: Interaction, user: Member = SlashOption(name="user", description="The Owner of the Carrier", required=True), carrierName: str = SlashOption(name="carrier_name", description="The Carrier that get's a new Owner"))
        await interaction.response.send_message("Carrier owner set!")