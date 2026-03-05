import discord
from discord import app_commands
from discord.ext import commands, tasks

class comandos(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
        
    @commands.command()
    async def somar(self, ctx:commands.Context, n1:float, n2:float):
        await ctx.reply(n1 + n2)    
        
async def setup(bot): #serve para inicializar a cog
    await bot.add_cog(comandos(bot))