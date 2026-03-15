import discord 
from discord.ext import commands
import aiohttp

class Anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    async def buscar_anime(self, nome:str):
        url = "https://graphql.anilist.co"
        query = """
        query ($nome: String) {
            Media(search: $nome, type: ANIME) {
                title { romaji english native }
                description(asHtml: false)
                averageScore
                episodes
                status
                coverImage { large }
                siteUrl
            }
        }
        """
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json={"query": query, "variables": {"nome": nome}}) as r:
                dados = await r.json()
                return dados["data"]["Media"]
            
    @commands.command()
    async def anime(self, ctx:commands.Context, *, nome:str):
        async with ctx.typing():
            dados = await self.buscar_anime(nome)
            if dados is None:
                return await ctx.reply("Não encontrei esse anime! 😢")
            
            titulo = dados["title"]["romaji"]
            descricao = dados["description"] or "Sem descrição disponível."
            nota = dados["averageScore"] or "N/A"
            episodios = dados["episodes"] or "?"
            status = dados["status"] or "?"
            capa = dados["coverImage"]["large"]
            link = dados["siteUrl"]

            embed = discord.Embed(title=titulo, url=link, color=discord.Color.blurple())
            embed.set_thumbnail(url=capa)
            embed.add_field(name="⭐ Nota", value=f"{nota}/100", inline=True)
            embed.add_field(name="📺 Episódios", value=episodios, inline=True)
            embed.add_field(name="📡 Status", value=status, inline=True)
            embed.add_field(name="📝 Sinopse", value=descricao[:500] + "..." if len(descricao) > 500 else descricao, inline=False)
            await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(Anime(bot))
            