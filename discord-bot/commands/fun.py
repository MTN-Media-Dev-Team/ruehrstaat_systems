from nextcord import Interaction

class FunCommands():
    def __init__(self, bot):
        self.bot = bot

        @bot.slash_command(name="ping", description="Ping Command")
        async def ping(interaction: Interaction):
            await interaction.response.send_message("Pong")