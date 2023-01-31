from nextcord import Interaction, SlashOption, Role, Permissions

class AdminCommands():
    def __init__(self, bot):
        self.bot = bot
        
        @bot.slash_command(name="registerrole", description="Registers a Role that can use a Bot", default_member_permissions=Permissions(administrator=True))
        async def regeisterRole(interaction: Interaction, roles: Role = SlashOption(name="roles", description="The Role that should be registered", required=True)):
            await interaction.response.send_message("Role registered")
