# TheHandOfFate
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from helpers import *
import asyncio

load_dotenv()
from dice_utils import *
from lookup_util import *
from d20 import roll

# get discord token from .env folder
TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix="$")

# bot commands

# help command
client.remove_command("help")


@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(colour=discord.Colour.green())
    embed.set_author(name="Help : list of commands available")
    embed.add_field(name="$dm", value="set the dm  ", inline=False)
    embed.add_field(
        name="$whisper / $w",
        value="whisper to a player\n  eg: $w @player you look very cute today",
        inline=False,
    )
    embed.add_field(
        name="$roll / $r", value="roll a dice \n    eg: $r 1d20 + 3", inline=False
    )
    embed.add_field(
        name="$reroll / $rr",
        value="roll a dice multiple times \n    eg: $rr 1 d20 + 3",
        inline=False,
    )
    embed.add_field(
        name="$secret / $s",
        value="make a secret roll \n    eg: $s 1 d20 + 3",
        inline=False,
    )
    await ctx.send(embed=embed)


# roll a dice once ex: $r 1d20 + 5
@client.command(pass_context=True, aliases=["r"])
async def rolling(ctx, *, input_message="1d20"):
    result = roll(input_message)
    str_header = (
        "**The Madam :** Let me blow on them for you "
        + ctx.message.author.mention
        + ":heart:\n"
        + "**Result: **"
    )
    await ctx.send(
        str_header
        + str(result).split("=")[0]
        + "**\nTotal : **"
        + "`"
        + str(result.total)
        + "`"
    )
    await ctx.message.delete()


# roll a dice multiple times  ex: $r 5 d20 + 5
@client.command(pass_context=True, aliases=["rr"])
async def reroll(ctx, number_of_rerols, *, input_message):
    result = format_roll(input_message, int(number_of_rerols))
    str_header = (
        "**The Madam :** Aw ~~ Quite the number of dice you're rolling "
        + ctx.message.author.mention
        + "... Let me help !\n"
    )
    await ctx.send(str_header + result)
    await ctx.message.delete()


@client.command(pass_context=True, aliases=["al"])
async def alias(ctx, commandTo, commandFrom):
    await ctx.send("This a test command")


@client.command(pass_context=True, aliases=["l"])
async def lookup(ctx, *, input_message):
    result, is_found = lookup_str(input_message)
    if is_found:
        for result in lookup_prepare(result):
            await ctx.send(embed=result)
    elif not result:
        await ctx.send("Input not found, Try again.")
    else:
        i = 0
        if len(result) >= 10:
            output = result[0:9]
        else:
            output = list(result)
        for i in range(0, len(output)):
            output[i] = "> " + "**[" + str(i + 1) + "]** : " + output[i]

        selection = await ctx.send("Did you mean : \n" + "".join(output))

        def check(m):
            return m.channel == ctx.message.channel and m.author == ctx.message.author

        try:
            msg = await client.wait_for("message", timeout=15, check=check)
            new_lookup = result[int(msg.content) - 1]
            await lookup(ctx, input_message=new_lookup[:-1])
            await msg.delete()
        except asyncio.TimeoutError:
            await ctx.send("Selection timed out.")
        finally:
            await selection.delete()


def lookup_prepare(result):
    """prepare an embed from a result"""
    try:
        body_text = result["body"]
    except Exception:
        body_text = " "
    if len(body_text) >= 2048:
        schunked_strings = chunks(body_text, 2048)
        embed = discord.Embed(
            title=result["name"],
            description=schunked_strings[0],
            url=result["src"],
            color=0xFF7000,
        )
        yield embed
        for string in schunked_strings[1:-1]:
            embed = discord.Embed(
                description=string,
                color=0xFF7000,
            )
            yield embed
        embed = discord.Embed(
            description=schunked_strings[-1],
            color=0xFF7000,
        )
    else:
        embed = discord.Embed(
            title=result["name"],
            description=body_text,
            url=result["src"],
            color=0xFF7000,
        )
    for key, value in result.items():
        if key in ["aon", "pfs", "src", "source", "name", "body"]:
            continue
        embed.add_field(name=key, value=value, inline=True)
    yield embed


# starting
client.run(TOKEN)