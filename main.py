import discord
from discord.ext import commands

import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f"Hai fatto l\\'accesso come {bot.user}")

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def rand(ctx):
    await ctx.send(random.randint(1, 10))

@bot.command()
async def mem(ctx):
    images = os.listdir("images")
    image = random.choice(images)
    print(image)
    with open(f'images/{image}', 'rb') as f:
        # Memorizziamo il file della libreria di Discord convertito in questa variabile!
        picture = discord.File(f)
   # Possiamo quindi inviare questo file come parametro!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una volta chiamato il comando duck, il programma richiama la funzione get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url) 

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def duck(ctx):
    '''Una volta chiamato il comando dog, il programma richiama la funzione get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url) 

# Evento di avvio del bot
@bot.event
async def on_ready():
    print(f'Bot is ready and logged in as {bot.user}')

# Comando per ottenere informazioni sull'inquinamento
@bot.command()
async def inquinamento(ctx):
    # Esempio di messaggio di risposta con informazioni sull'inquinamento
     await ctx.send("L'inquinamento atmosferico è un problema globale che riguarda l'emissione di sostanze nocive nell'aria, come gas serra e particolato fine. Questo può causare danni alla salute umana e all'ambiente. È importante adottare misure per ridurre l'inquinamento, come l'uso di energie rinnovabili, il miglioramento dell'efficienza energetica e la promozione dei trasporti pubblici.")

    
bot.run("MTE1ODc5MjMxNjQ4ODc4NjAzMQ.GhVIVd.XRVMdUciqoWI9mlq8PSEPktIyp0u4sPXtnNWU8")
