import os
import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="!")

@bot.command()
async def hello(ctx):
  await ctx.send("Hello!")

@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@bot.command()
async def 


































my_secret = os.environ['token']
bot.run(my_secret)