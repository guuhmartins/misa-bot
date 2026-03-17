import discord 
from discord.ext import commands
from deep_translator import GoogleTranslator
import asyncio

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    async def calcular(self, ctx:commands.Context, *, expressao:str):
        try:
            resultado = eval(expressao, {"__builtins__": {}})
            await ctx.reply(f"🧮 `{expressao}` = **{resultado}**")
        except:
            await ctx.reply("❌ Expressão inválida!")

    @commands.command()
    async def traduzir(self, ctx:commands.Context, *, texto:str):
        try:
            traducao = GoogleTranslator(source="auto", target="pt").translate(texto)
            await ctx.reply(f"🌐 **Tradução:**\n{traducao}")
        except:
            await ctx.reply("❌ Não consegui traduzir!")

    @commands.command()
    async def remind(self, ctx:commands.Context, tempo:str, *, mensagem:str):
        unidades = {"s": 1, "m": 60, "h": 3600}
        unidade = tempo[-1]
        if unidade not in unidades:
            return await ctx.reply("❌ Use: `.remind 10m estudar` (s/m/h)")
        try:
            quantidade = int(tempo[:-1])
        except:
            return await ctx.reply("❌ Tempo inválido!")
        segundos = quantidade * unidades[unidade]
        await ctx.reply(f"⏰ Lembrete definido! Te aviso em **{tempo}**!")
        await asyncio.sleep(segundos)
        await ctx.author.send(f"⏰ Lembrete: **{mensagem}**")

async def setup(bot):
    await bot.add_cog(Utils(bot))