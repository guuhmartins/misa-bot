import discord
from discord.ext import commands
from database import conectar

class Moderacao(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
        
    @commands.command()
    @commands.has_role("Misa Owner")
    async def clear(self, ctx:commands.Context, quantidade:int=10):
        await ctx.channel.purge(limit=quantidade + 1)
        await ctx.send(f"🗑️ {quantidade} mensagens apagadas!", delete_after=3)
        
    @commands.command()
    @commands.has_role("Misa Owner")
    async def slow(self, ctx:commands.Context, segundos:int=0):
        await ctx.channel.edit(slowmode_delay=segundos)
        if segundos == 0:
            await ctx.reply("Slowmode desativado!")
        else:
            await ctx.reply(f"Slowmode definido para **{segundos}**!")
            
    @commands.command()
    @commands.has_role("Misa Owner")
    async def lock(self, ctx:commands.Context):  
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.reply("Canal Travado!")
        
    @commands.command()
    @commands.has_role("Misa Owner")
    async def unlock(self, ctx:commands.Context):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.reply("Canal Destravado!")

    @commands.command()
    @commands.has_role("Misa Owner")
    async def warn(self, ctx:commands.Context, membro:discord.Member, *, motivo:str="Sem motivo"):
        conn = conectar()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO warns (usuario_id, servidor_id, motivo, moderador_id)
            VALUES (%s, %s, %s, %s)
        """, (membro.id, ctx.guild.id, motivo, ctx.author.id))
        
        conn.commit()
        
        cursor.execute("""
            SELECT COUNT(*) FROM warns
            WHERE usuario_id = %s AND servidor_id = %s
        """, (membro.id, ctx.guild.id))
        
        total = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        
        await ctx.reply(f"⚠️ {membro.mention} recebeu um warn! Total: **{total}/5** | Motivo: {motivo}")
        
        if total >= 3:
            await membro.timeout(discord.utils.utcnow() + discord.timedelta(minutes=10))
            await ctx.send(f"🔇 {membro.mention} foi silenciado por acumular 3 warns!")
        
        if total >= 5:
            await membro.ban(reason="5 warns acumulados")
            await ctx.send(f"🔨 {membro.mention} foi banido por acumular 5 warns!")

    @commands.command()
    @commands.has_role("Misa Owner")
    async def warnings(self, ctx:commands.Context, membro:discord.Member):
        conn = conectar()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT motivo, moderador_id, data FROM warns
            WHERE usuario_id = %s AND servidor_id = %s
            ORDER BY data DESC
        """, (membro.id, ctx.guild.id))
        
        resultado = cursor.fetchall()
        cursor.close()
        conn.close()
        
        if not resultado:
            return await ctx.reply(f"{membro.mention} não tem warns! ✅")
        
        embed = discord.Embed(
            title=f"⚠️ Warns de {membro.display_name}",
            color=discord.Color.yellow()
        )
        
        for i, (motivo, moderador_id, data) in enumerate(resultado, 1):
            embed.add_field(
                name=f"Warn #{i}",
                value=f"Motivo: {motivo}\nData: {data.strftime('%d/%m/%Y')}",
                inline=False
            )
        
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_role("Misa Owner")
    async def clearwarns(self, ctx:commands.Context, membro:discord.Member):
        conn = conectar()
        cursor = conn.cursor()
        
        cursor.execute("""
            DELETE FROM warns
            WHERE usuario_id = %s AND servidor_id = %s
        """, (membro.id, ctx.guild.id))
        
        conn.commit()
        cursor.close()
        conn.close()
        
        await ctx.reply(f"✅ Warns de {membro.mention} foram limpos!")
        
async def setup(bot):
    await bot.add_cog(Moderacao(bot))  