import discord 
from discord.ext import commands, tasks
import os

intents = discord.Intents.all() #permissoes do discord
bot = commands.Bot(".", intents=intents) #prefixo, recebendo permissoes

async def carregar_cogs():
    for arquivo in os.listdir('cogs'): #para cada lop do for a var arquivo vai receber um nome conforme os itens passados entre argumentos
        if arquivo.endswith('.py'): 
            await bot.load_extension(f"cogs.{arquivo[:-3]}") #funcao pra carregar, excluindo a extensao do arquivo
        
@bot.event
async def on_ready():
    await carregar_cogs()
    await bot.tree.sync()
    print("estou pronto!")
    
    await bot.change_presence(      
        status=discord.Status.online
    )
    
    await bot.change_presence(                              #listening caso queira alterar para escutando.
        activity=discord.Activity(type=discord.ActivityType.watching, name='Hunter X Hunter! EP 72')
    )

bot.run("TOKEN DO BOT") #starta o bot