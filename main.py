# TheHandOfFate
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from util import * 
from helpers import *
load_dotenv()
from dice_utils import *

#get discord token from .env folder
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = '$')



# general functions 

# sending a dm to the dm
async def dmDm(message):
    dm = client.get_user(getDM())
    await dm.send(message)

#forward the whisper to the Dm 
async def forwardMessage(message,user1,user2):
    message=user1.mention + " whispers to " + user2.mention + ": " + message
    await dmDm(message)

#bot commands

#help command
client.remove_command('help')
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed.set_author(name='Help : list of commands available')
    embed.add_field(name='$dm', value='set the dm  ', inline=False)
    embed.add_field(name='$whisper / $w', value='whisper to a player ', inline=False)
    await ctx.send(embed=embed)

#sent the dm of the campaign 
@client.command(pass_context=True)
async def dm(ctx, user: discord.User): 
    strUser = user.id
    setDM(strUser)
    await ctx.send(user.mention + " is now The Mighty DM , Time for adventure ")

#whisper to another player
@client.command(pass_context=True,aliases=['w'])
async def whisper(ctx, user: discord.User, *, input_message=None):
    input_message = input_message or "This Message is sent via DM"
    message = "whisper from "+ ctx.message.author.mention + " : " + input_message
    await user.send(message)
    message = ctx.message
    await message.delete()
    await forwardMessage(input_message,ctx.message.author,user)

@client.command(pass_context=True,aliases=['r'])
async def roll(ctx,*,input_message):
    result = roll_command(input_message)
    await ctx.send("**The Madam :** Let me blow on them for you :heart:")
    await ctx.send(result)

@client.command(pass_context=True,aliases=['s'])
async def secret(ctx,*,input_message):
    result = roll_command(input_message)
    header_string = ctx.message.author.mention + " rolled a secret check :\n"
    await ctx.send("**The Madam :** Spoilers ... ")
    await dmDm(header_string+result)


#starting 
client.run(TOKEN)
