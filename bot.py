import config, cargar, discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents= intents, command_prefix= "?")
exec(cargar.cargar_eventos())
eventos(bot)
bot.run(config.token)