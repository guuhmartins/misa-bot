import discord
from discord import app_commands
from discord.ext import commands, tasks

class comandos(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
        
    @commands.command()
    async def ola(self, ctx:commands.Context):
        nome = ctx.author.name
        await ctx.reply(f"ola, {nome}! tudo bem?")   
        
async def setup(bot): #serve para inicializar a cog
    await bot.add_cog(comandos(bot))