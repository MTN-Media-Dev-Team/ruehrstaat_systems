from nextcord import Interaction, SlashOption, SelectOption
from nextcord.ui import Select, View, TextInput, Modal

from helpfunctions import formatCarrierName
from caching import getCarrierObjectByName

from permission import isUserAdmin

def initCaptainCommands(bot, args_dict):
        
    TESTING_GUILD_ID = args_dict["TESTING_GUILD_ID"]
    
    @bot.slash_command(name="editcarrier", description="Edit your own carrier (Captains only)", guild_ids=[TESTING_GUILD_ID])
    async def editcarrier(interaction: Interaction, carrierName: str = SlashOption(name="carrier_name", description="The Carrier that get's a new Owner")):
        carrierName = formatCarrierName(carrierName)
        if not carrierName:
            await interaction.response.send_message("Carrier not found!", ephemeral=True)
            return

        carrier = getCarrierObjectByName(carrierName)

        if not isUserAdmin(interaction.user) and interaction.user.id != carrier.ownerDiscordID:
            await interaction.response.send_message("You are not the Captain!", ephemeral=True)
            return

        options = ["Edit Location"]

        selectOption = Select(placeholder="Select an option", options=[SelectOption(label=option, value=option) for option in options])
        selectmessage = None

        async def callback(interaction: Interaction):
            # get carrier id
            option = selectOption.values[0]
            if carrier == None:
                await interaction.response.send_message("Carrier not found!", ephemeral=True)
                return
            if option == "Edit Location":
                await selectmessage.delete()

                class InputModal(Modal):
                    def __init__(self):
                        super().__init__(title="Enter a new Location")
                        self.textInput = TextInput(label="Enter a new Location", placeholder="Sol", custom_id="textinput")
                        self.add_item(self.textInput)

                    async def callback(self, interaction: Interaction):
                        carrier.setCarrierLocation(self.textInput.value)
                        await interaction.response.send_message(f"Location of carrier {carrierName} changed to {self.textInput.value}!", ephemeral=True) 

                await interaction.response.send_modal(InputModal())

        selectOption.callback = callback
        view = View()
        view.add_item(selectOption)
        selectmessage = await interaction.response.send_message(f"Select an option for carrier {carrierName}", view=view, ephemeral=True)
  
        
    


        
