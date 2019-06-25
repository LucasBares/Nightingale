import os

from discord import Game
from discord.ext.commands import Bot

bot = Bot(command_prefix='.')

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=Game("with humans"))
    print("Logged in as " + bot.user.name)

# Commands
@bot.command()
async def test(ctx):
    await ctx.send("Test!")

bot.run(os.environ["BOT_TOKEN"])