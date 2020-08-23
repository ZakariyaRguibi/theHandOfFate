# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

#get discord token from .env folder
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = '$')

#adding commands
@client.command()
async def lickass(ctx):
    await ctx.send("fate is very nice")

client.remove_command('help')

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed.set_author(name='Help : list of commands available')
    embed.add_field(name='$lickass', value='complimenting the one in charge for xp', inline=False)
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def dm(ctx, user: discord.User, *, message=None):
    message = message or "This Message is sent via DM"
    await user.send(message)

#starting
client.run(TOKEN)
