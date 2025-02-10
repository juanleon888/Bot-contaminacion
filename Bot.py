import discord
from discord.ext import commands
from bot_logic import*
import os,random
import requests 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'estamos dentro {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Bienvenido hoy aprenderemos de educación ambiental, soy un chatbot {bot.user}! , estos son mis comandos $limpiar, $heh.  ')

#Limpiar
@bot.command()
async def reciclar(ctx):
    await ctx.send("Es tiempo de enseñarte a reciclar")



bot.run ()
