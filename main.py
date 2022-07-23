import os
import discord
import music
import asyncio
import keep_alive
from discord.ext import commands


bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

#----------------------MODERATION COMMANDS--------------------------------------------


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
            await member.send(member.name + "has been unbanned from the Community!")
            return


#The below code Softbans a Person for a Certain Amount of Time.
@bot.command()
async def softban(ctx, user:discord.User, duration: int):
    await ctx.guild.ban(user)
    await asyncio.sleep(duration)
    await ctx.guild.unban(user)


          
#------------------------------------------------Music Bot-------------------------------------------
cogs = [music]

for i in range(len(cogs)):
  cogs[i].setup(bot)

#--------------------NORMAL COMMANDS---------------------------------------------

#Creates a Two Option Yes or No Poll
@bot.command()
async def poll(ctx, *, content:str):
  print("Creating yes/no poll...")
  embed=discord.Embed(title=f"{content}", description="React to this message with ✅ for yes, ❌ for no.",  color=0xd10a07)
  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url) 
  print("Embed created")
  message = await ctx.channel.send(embed=embed)
  await message.add_reaction("✅")
  await message.add_reaction("❌")


#Ping Commands which gives the Latency of the Bot
@bot.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    
    latency = bot.latency
    await ctx.send(f'The ping of the bot is:')
    await ctx.send(latency)




#Mentions the ServerInformation
@bot.command(help = "Prints details of Server")
async def where_am_i(ctx):
    owner=str(ctx.guild.owner)
    region = str(ctx.guild.region)
    guild_id = str(ctx.guild.id)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)
    desc=ctx.guild.description
    
    embed = discord.Embed(
        title=ctx.guild.name + " Server Information",
        description=desc,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=guild_id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

    members=[]
    async for member in ctx.guild.fetch_members(limit=150) :
        await ctx.send('Name : {}\t Status : {}\n Joined at {}'.format(member.display_name,str(member.status),str(member.joined_at)))

@bot.command()
async def tell_me_about_yourself(ctx):
    text = "My name is MasterBot!\n I was built by MST :)"
    await ctx.send(text)



#Mentions the User Information
@bot.command()
async def userinfo(ctx, *, user: discord.Member = None):
    if isinstance(ctx.channel, discord.DMChannel):
      return
    if user is None:
      user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=0xdfa3ff, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join position", value=str(members.index(user)+1))
    embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    embed.add_field(name="Guild permissions", value=perm_string, inline=False)
    embed.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=embed)






































keep_alive.keep_alive()
my_secret = os.environ['token']
bot.run(my_secret)