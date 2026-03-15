import discord
from discord.ext import commands
import random
import aiohttp
import os

class Diversao(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    async def buscar_gif(self, termo:str):
        async with aiohttp.ClientSession() as session:
            url = "https://api.giphy.com/v1/gifs/search"
            params = {
                "api_key": os.getenv("GIPHY_KEY"),
                "q": termo,
                "limit": 10,
                "rating": "g"
            }
            async with session.get(url, params=params) as resposta:
                dados = await resposta.json()
                gifs = dados["data"]
                if not gifs:
                    return None
                gif = random.choice(gifs)
                return gif["images"]["original"]["url"]

    @commands.command()
    async def hug(self, ctx, membro:discord.Member=None):
        gif = await self.buscar_gif("anime hug")
        if gif is None:
            return await ctx.reply("Não encontrei nenhum GIF! 😢")
        if membro:
            descricao = f"{ctx.author.mention} abraçou {membro.mention}! 🤗"
        else:
            descricao = f"{ctx.author.mention} quer um abraço! 🤗"
        embed = discord.Embed(description=descricao)
        embed.set_image(url=gif)
        await ctx.reply(embed=embed)

    @commands.command()
    async def kiss(self, ctx, membro:discord.Member=None):
        gif = await self.buscar_gif("anime kiss")
        if gif is None:
            return await ctx.reply("Não encontrei nenhum GIF! 😢")
        if membro:
            descricao = f"{ctx.author.mention} deu um beijo em {membro.mention}! 💋"
        else:
            descricao = f"{ctx.author.mention} jogou um beijo pro ar! 💋"
        embed = discord.Embed(description=descricao)
        embed.set_image(url=gif)
        await ctx.reply(embed=embed)

    @commands.command()
    async def cafune(self, ctx, membro:discord.Member=None):
        gif = await self.buscar_gif("anime head pat")
        if gif is None:
            return await ctx.reply("Não encontrei nenhum GIF! 😢")
        if membro:
            descricao = f"{ctx.author.mention} fez cafuné em {membro.mention}! 🥰"
        else:
            descricao = f"{ctx.author.mention} quer cafuné! 🥰"
        embed = discord.Embed(description=descricao)
        embed.set_image(url=gif)
        await ctx.reply(embed=embed)

    @commands.command()
    async def highfive(self, ctx, membro:discord.Member=None):
        gif = await self.buscar_gif("anime high five")
        if gif is None:
            return await ctx.reply("Não encontrei nenhum GIF! 😢")
        if membro:
            descricao = f"{ctx.author.mention} deu um high five pra {membro.mention}! ✋"
        else:
            descricao = f"{ctx.author.mention} quer dar um high five! ✋"
        embed = discord.Embed(description=descricao)
        embed.set_image(url=gif)
        await ctx.reply(embed=embed)

    @commands.command()
    async def attack(self, ctx, membro:discord.Member=None):
        gif = await self.buscar_gif("anime attack")
        if gif is None:
            return await ctx.reply("Não encontrei nenhum GIF! 😢")
        if membro:
            descricao = f"{ctx.author.mention} atacou {membro.mention}! ⚔️"
        else:
            descricao = f"{ctx.author.mention} tá atacando o ar! ⚔️"
        embed = discord.Embed(description=descricao)
        embed.set_image(url=gif)
        await ctx.reply(embed=embed)

    @commands.command()
    async def dance(self, ctx, membro:discord.Member=None):
        gif = await self.buscar_gif("anime dance")
        if gif is None:
            return await ctx.reply("Não encontrei nenhum GIF! 😢")
        if membro:
            descricao = f"{ctx.author.mention} dançou com {membro.mention}! 💃"
        else:
            descricao = f"{ctx.author.mention} tá dançando sozinho! 💃"
        embed = discord.Embed(description=descricao)
        embed.set_image(url=gif)
        await ctx.reply(embed=embed)

    @commands.command()
    async def laugh(self, ctx, membro:discord.Member=None):
        gif = await self.buscar_gif("anime laugh")
        if gif is None:
            return await ctx.reply("Não encontrei nenhum GIF! 😢")
        if membro:
            descricao = f"{ctx.author.mention} riu de {membro.mention}! 😂"
        else:
            descricao = f"{ctx.author.mention} tá rindo muito! 😂"
        embed = discord.Embed(description=descricao)
        embed.set_image(url=gif)
        await ctx.reply(embed=embed)

    @commands.command()
    async def cry(self, ctx, membro:discord.Member=None):
        gif = await self.buscar_gif("anime cry")
        if gif is None:
            return await ctx.reply("Não encontrei nenhum GIF! 😢")
        if membro:
            descricao = f"{ctx.author.mention} chorou por {membro.mention}! 😢"
        else:
            descricao = f"{ctx.author.mention} tá chorando! 😢"
        embed = discord.Embed(description=descricao)
        embed.set_image(url=gif)
        await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(Diversao(bot))