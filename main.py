import os
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="!")

#----------------------BOT COMMANDS------------------------------------------------------------


#This code will clear messages!
@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount) #Will clear messages from the Discord Channel


#This code will reply when command error!
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the requirements :angry:")

      
#The below code Kicks People!
@bot.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "No Reason Provided"):
  await member.send("You have been kicked from the Community, Because:"+reason)
  await member.kick(reason=reason)

      
#The below code bans player.
@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = "No reason Provided"):
    await member.ban(reason = reason)
    await member.send(member.name + "has been banned from the Community, because:"+reason)

  
#The below code unbans player.
@bot.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return
































my_secret = os.environ['token']
bot.run(my_secret)