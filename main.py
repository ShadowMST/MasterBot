import os
import discord
from discord.ext import commands
import asyncio

from commands import *
from events import *

bot = commands.Bot(command_prefix="!")

@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount) #Will clear messages from the Discord Channel

my_secret = os.environ['token']
bot.run(my_secret)