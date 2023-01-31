from nextcord import Interaction, SlashOption

class CarrierCommands():
    def __init__(self, bot):
        self.bot = bot
        
        @bot.slash_command(name="registercarrierinfo", description="Registers a new Carrier Info Channel")
        async def test(interaction: Interaction, arg1: str = SlashOption(name="1234", description="Ich bin ein Test", required=True)):
            await interaction.response.send_message("Test")

