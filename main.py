import discord
import os
import datetime
from keep_alive import keep_alive
from discord.ext import commands
my_secret = os.environ['Token']

# client = discord.Client()
# test
bot = commands.Bot(command_prefix='!')
@bot.command(pass_context=True,
	help="Update the role of user if you have Admin role eg: !updaterole 'xyz#0000' 'Admin'.",
	brief="-Update the role of user."
)
@commands.has_role("Admin")
async def updaterole(ctx, user: discord.Member, role,help="This is role"):
    member = user
    
    print(member)
    var = discord.utils.get(ctx.guild.roles, name = role)
    print(var)
    await member.add_roles(var)
    await ctx.send(f'Role `{member}` has been Asigned with role {role}')
@bot.command(aliases=['make_role'],	help="-Update the role of user if you have Admin role eg: !make_role 'XYZ' ",
	brief="-Update the role of user."
)
@commands.has_permissions(manage_roles=True) # Check if the user executing the command can manage roles
async def create_role(ctx, name):
	guild = ctx.guild
	await guild.create_role(name=name)
	await ctx.send(f'Role `{name}` has been created')
  
@bot.command(name="Poro",help="-Type Poro with prefix of '!' to comunicate with me . ")
async def x(ctx):
  emoji = '\N{THUMBS UP SIGN}'
  # member = ctx.author
  await ctx.send(f"Hello {ctx.author} am Poro and i like you {emoji}. :")
  
  # guild = ctx.guild
  # await guild.create_role(name="role name") 
  
async def on_ready():
  print(f"{bot.user.name} has connected With you !")
@bot.command(name="create_channel",help="-to create channel eg:!create_channel 'XYZ'")
@commands.has_role("Admin")
async def create_Channel(xx,channel_name):
  guild=xx.guild
  existing_channel=discord.utils.get(guild.channels, name=channel_name)
  if not existing_channel:
    print(f"created new channel:{channel_name}")
    await guild.create_text_channel(channel_name)
    await xx.send(f"i have create channel with name {channel_name} channel created by {xx.author} on {datetime.datetime.now()}")
# @client.event
# async def on_ready():
#     print(f'{client.user.name} has connected to Discord!')

# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )

# # client.run(my_secret)
# @client.event
# async def on_message(message):
#   if message.author== client.user:
#     return
  
#   if message.content.startswith("$hello"):
#     await message.channel.send(f"Hello! {message.author}")
  
keep_alive() 
bot.run(my_secret)