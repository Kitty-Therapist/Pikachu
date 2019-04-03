import discord
import datetime
from discord.ext import commands
from discord import utils

TOKEN = "memes"

bot = commands.Bot(command_prefix = "!")

bot.starttime = datetime.datetime.now()
bot.startup_done = False

initial_extensions = ['basic']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(f"cogs.{extension}")


@bot.event
async def on_ready():
        print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}' + f'\nVersion: {discord.__version__}\n')

bot.run(TOKEN)
