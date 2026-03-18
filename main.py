import discord 
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default() #permissoes basicas do discord
intents.members = True
intents.message_content = True

class MisaBot(commands.Bot):  
    def __init__(self): #construtor 
        super().__init__(command_prefix=".", intents=intents) #prefixo, recebendo permissoes
    
    async def setup_hook(self):
        from database import conectar
        conectar()
        await carregar_cogs(self)
        await self.tree.sync()
        print("Cogs carregadas!")
        
        for guild in self.guilds:
            await guild.chunk()   

    async def on_ready(self):
        print(f"Misa está pronta! Logada como {self.user}")
        await self.change_presence(
            status=discord.Status.online,
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name='Hunter X Hunter! EP 72'
            )
        )
        
async def carregar_cogs(bot):
    for arquivo in os.listdir('cogs'):
        if arquivo.endswith('.py'):
            await bot.load_extension(f"cogs.{arquivo[:-3]}") 
            
bot = MisaBot()
bot.run(TOKEN)    
        