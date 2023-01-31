import configparser
from commands import carrier, admin, fun
from nextcord.ext import commands

config = configparser.ConfigParser()
config.read('config.ini')

config.sections()

bot_token = config['DISCORD']['bot_token']

bot = commands.Bot()

carrier.CarrierCommands(bot)
admin.AdminCommands(bot)
fun.FunCommands(bot)

bot.run(bot_token)

