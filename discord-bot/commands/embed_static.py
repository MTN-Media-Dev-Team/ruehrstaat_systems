from nextcord import Interaction, SelectOption
from nextcord.ui import Select, View
from caching import getAllCarrierNames, getCarrierObjectByID
import logging

from embeds import getCarrierInfoStaticEmbed

# set the channel of an specific carrier with the carrier id and the channel id 

def initEmbedCommands(bot, args_dict):


    TESTING_GUILD_ID = args_dict["TESTING_GUILD_ID"]
    db = args_dict["db"]
    cursor = db.cursor
    # Carrier channel command to set the channel for the static embeds

    @bot.slash_command(name="setcarrierchannel", description="Sets the channel for the static embeds", guild_ids=[TESTING_GUILD_ID])
    async def setcarrierchannel(interaction: Interaction):
        #get all carrier names
        carrierNames = getAllCarrierNames()
        selectCarrier = Select(placeholder="Select a Carrier", options=[SelectOption(label=carrierNames[carrier], value=carrier) for carrier in carrierNames])

        selectmessage = None 

        async def callback(interaction: Interaction):
            # get carrier id
            carrier_id = selectCarrier.values[0]
            if carrier_id == None:
                await interaction.response.send_message("Carrier not found!", ephemeral=True)
                return
            await selectmessage.delete()
            channel = interaction.channel
            guild_id = interaction.guild.id
            guild_id = interaction.guild.id
            cursor.execute("SELECT * FROM guilds WHERE guild_id = ? AND carrier_id = ?", (guild_id, carrier_id))
            guild = cursor.fetchone()
            if guild == None:
                cursor.execute("INSERT INTO guilds (guild_id, carrier_channel_id, carrier_id) VALUES (?,?,?)", (guild_id,channel.id,carrier_id))
            else:
                cursor.execute("UPDATE guilds SET carrier_channel_id = ? WHERE guild_id = ? AND carrier_id = ?", (channel.id, guild_id, carrier_id))                
            db.connection.commit()
            logging.info(f"Carrier channel set to {channel.id} for guild {guild_id}")
            await interaction.response.send_message(f"Carrier Channel Set for Carrier " + getCarrierObjectByID(carrier_id).name, ephemeral=True)
            embed, view = getCarrierInfoStaticEmbed(carrier_id)
            await channel.send(embed=embed, view=view)
            
            return None

        selectCarrier.callback = callback
        view = View()
        view.add_item(selectCarrier)
        selectmessage = await interaction.response.send_message("Select a Carrier", view = view, ephemeral=True) 

            



    
# carrier refresh method to refresh the static embeds with args from the websocket event or nothing to refresh all
def refreshCarrierEmbeds(bot, args_dict, carrier_id=None):
    db = args_dict["db"]
    cursor = db.cursor
    logging.info("refreshing carrier embeds")
    cursor.execute("SELECT * FROM guilds WHERE carrier_id = ?", (carrier_id))
    db_object = cursor.fetchone()
    embed, view = getCarrierInfoStaticEmbed(carrier_id)
    bot.getChannel(db_object.carrier_channel_id).send(embed=embed, view=view)
    