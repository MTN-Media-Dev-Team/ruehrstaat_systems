from nextcord import Interaction, SlashOption

def initCarrierCommands(bot, args_dict):
        
    TESTING_GUILD_ID = args_dict["TESTING_GUILD_ID"]

    @bot.slash_command(name="test", description="test", guild_ids=[TESTING_GUILD_ID])
    async def test(interaction: Interaction, arg1: str = SlashOption(name="1234", description="Ich bin ein Test", required=True)):
        await interaction.response.send_message("Test")
    
    @bot.slash_command(name="carrierinfo", description="Get Information about an specific Squadron Carrier", guild_ids=[TESTING_GUILD_ID])
    async def carrierinfo(interaction: Interaction, arg1: str= SlashOption(name="Carrier", required=True)):
        await interaction.response.send_message("I am a Placeholder")


