from dis import dis
import discord
from discord.ext import commands
import ptowers
import pmines
import proulette
import fmines
import random

#client = discord.Client(intents=discord.Intents.all())
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.command(name="ptowers")
async def towers(context):
    if isinstance(context.channel, discord.channel.DMChannel):
        pass
    
    else:
        if context.channel.id == 1015730002542739557 or context.channel.id == 1015948438568972411 or context.channel.id == 1015948506453786634:
        
            acc = random.uniform(33, 66)

            tEmbed = discord.Embed(title="Samurai Predictions", color=0x00ff00)
            tEmbed.add_field(name="Prediction", value=ptowers.ptowers(), inline=False)
            tEmbed.add_field(name="Accuracy", value=round(acc, 2), inline=False)    
            
            await context.message.channel.send(embed=tEmbed)
        else:
            pass

@client.command(name="pmines")
async def mines(context):
    if isinstance(context.channel, discord.channel.DMChannel):
        pass
    
    else:
        if context.channel.id == 1015730002542739557 or context.channel.id == 1015948438568972411 or context.channel.id == 1015948506453786634:
            acc = random.uniform(50, 80)

            mEmbed = discord.Embed(title="Samurai Predictions", color=0x00ff00)
            mEmbed.add_field(name="Prediction", value=pmines.pmines(), inline=False)
            mEmbed.add_field(name="Accuracy", value=round(acc, 2), inline=False) 

            await context.message.channel.send(embed=mEmbed)
        else:
            pass

@client.command(name="proulette")
async def roulette(context):
    if isinstance(context.channel, discord.channel.DMChannel):
        pass
    
    else:
        if context.channel.id == 1015730002542739557 or context.channel.id == 1015948438568972411 or context.channel.id == 1015948506453786634:
            acc = random.uniform(35, 50)

            rEmbed = discord.Embed(title="Samurai Predictions", color=0x00ff00)
            rEmbed.add_field(name="Prediction", value=proulette.proulette(), inline=False)
            rEmbed.add_field(name="Accuracy", value=round(acc, 2), inline=False) 

            await context.message.channel.send(embed=rEmbed)
        else:
            pass

@client.command(name="fmines")
async def mines(context):
    if context.channel.id == 1015615108115857438 or context.channel.id == 1015615149870157826 or context.channel.id == 1015615168916492348:
        acc = random.uniform(35, 50)

        rEmbed = discord.Embed(title="Samurai Predictions", color=0x00ff00)
        rEmbed.add_field(name="Prediction", value=fmines.fmines(), inline=False)
        rEmbed.add_field(name="Accuracy", value=round(acc, 2), inline=False) 

        await context.message.channel.send(embed=rEmbed)
    else:

        await context.message.channel.send("This command doesn't work in this channel, use #commands-1 , #commands-2 or #commands-3")

@client.command(name="fcrash")
async def crash(context):
    if context.channel.id == 1015615108115857438 or context.channel.id == 1015615149870157826 or context.channel.id == 1015615168916492348:
        await context.message.channel.send("Crash isnt developed yet. You can use:\n!fmines")
    else:
        await context.message.channel.send("This command doesn't work in this channel, use #commands-1 , #commands-2 or #commands-3")

@client.command(name="ftowers")
async def crash(context):
    if context.channel.id == 1015615108115857438 or context.channel.id == 1015615149870157826 or context.channel.id == 1015615168916492348:
        await context.message.channel.send("Towers is only in the premium version of the predictor. Make a ticket to purchase premium")
    else:
        await context.message.channel.send("This command doesn't work in this channel, use #commands-1 , #commands-2 or #commands-3")

@client.command(name="test")
async def testing(context):
    acc = random.uniform(35, 50)

    rEmbed = discord.Embed(title="Samurai Predictions", color=0x00ff00)
    rEmbed.add_field(name="Prediction", value=fmines.fmines(), inline=False)
    rEmbed.add_field(name="Accuracy", value=round(acc, 2), inline=False) 

    emoji = '\N{THUMBS UP SIGN}'
    await context.message.channel.send(embed=rEmbed)
    
      
client.run("MTAxNTY3ODAxNjMyOTg5NTk2Nw.Gb_Ozr.Sy75Z8wasrlJ6YeOoIH6twMmN8CK8gqPPLghng")
