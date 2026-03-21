import discord
from discord.ext import commands
import random
import time
from database import conectar

class XP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
        self.cooldowns = {}

        self.cargos_nivel = {
            15: "Apprentice",
            50: "Adventurer",
            100: "Elite",
            150: "Champion",
            250: "Legend",
            300: "Mythic"
        }

    @commands.Cog.listener()
    async def on_message(self, mensagem:discord.Message):
        if mensagem.author.bot:
            return
        if mensagem.guild is None:
            return
        
        agora = time.time()
        usuario_id = mensagem.author.id
        servidor_id = mensagem.guild.id

        ultimo = self.cooldowns.get(usuario_id, 0)
        if agora - ultimo < 60:
            return
        
        self.cooldowns[usuario_id] = agora
        xp_ganho = random.randint(15, 25)
        
        try:
            conn = conectar()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO xp (usuario_id, servidor_id, xp, nivel, ultima_mensagem)
                VALUES (%s, %s, %s, 1, NOW())
                ON DUPLICATE KEY UPDATE
                xp = xp + %s,
                ultima_mensagem = NOW()
            """, (usuario_id, servidor_id, xp_ganho, xp_ganho))
            
            conn.commit()
            print(f"✅ XP salvo: {xp_ganho} XP para {usuario_id}")

            cursor.execute("""
                SELECT xp, nivel FROM xp
                WHERE usuario_id = %s AND servidor_id = %s
            """, (usuario_id, servidor_id))
            
            resultado = cursor.fetchone()
            cursor.close()
            conn.close()

        except Exception as e:
            print(f"❌ Erro ao salvar XP: {e}")
            return

        if resultado:
            xp_atual, nivel_atual = resultado
            xp_necessario = nivel_atual * 100
            
            if xp_atual >= xp_necessario:
                try:
                    conn2 = conectar()
                    cursor2 = conn2.cursor()
                    novo_nivel = nivel_atual + 1
                    cursor2.execute("""
                        UPDATE xp SET nivel = %s, xp = 0
                        WHERE usuario_id = %s AND servidor_id = %s
                    """, (novo_nivel, usuario_id, servidor_id))
                    conn2.commit()
                    cursor2.close()
                    conn2.close()
                except Exception as e:
                    print(f"❌ Erro ao subir nível: {e}")
                    return
                
                await mensagem.channel.send(
                    f"🎉 {mensagem.author.mention} subiu para o **nível {novo_nivel}**!"
                )
                
                if novo_nivel in self.cargos_nivel:
                    nome_cargo = self.cargos_nivel[novo_nivel]
                    cargo = discord.utils.get(mensagem.guild.roles, name=nome_cargo)
                    if cargo:
                        await mensagem.author.add_roles(cargo)
                        await mensagem.channel.send(
                            f"🏆 {mensagem.author.mention} desbloqueou o cargo **{nome_cargo}**!"
                        )

    @commands.command()
    async def xp(self, ctx:commands.Context, membro:discord.Member=None):
        if membro is None:
            membro = ctx.author
        
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT xp, nivel FROM xp
            WHERE usuario_id = %s AND servidor_id = %s
        """, (membro.id, ctx.guild.id))
        
        resultado = cursor.fetchone()
        
        cursor.execute("""
            SELECT COUNT(*) FROM xp
            WHERE servidor_id = %s AND xp > (
                SELECT xp FROM xp WHERE usuario_id = %s AND servidor_id = %s
            )
        """, (ctx.guild.id, membro.id, ctx.guild.id))
        
        posicao = cursor.fetchone()[0] + 1
        cursor.close()
        conn.close()
        
        if resultado is None:
            return await ctx.reply("Esse membro ainda não tem XP! 😢")
        
        xp_atual, nivel_atual = resultado
        xp_necessario = nivel_atual * 100
        xp_faltando = xp_necessario - xp_atual
        proximo_cargo = None
        
        for nivel, cargo in self.cargos_nivel.items():
            if nivel > nivel_atual:
                proximo_cargo = cargo
                break
        
        embed = discord.Embed(
            title=f"⭐ | Informações de XP",
            color=discord.Color.blurple()
        )
        embed.set_thumbnail(url=membro.display_avatar.url)
        embed.add_field(name="👤 Membro", value=membro.display_name, inline=False)
        embed.add_field(name="🏅 Nível Atual", value=f"Nível {nivel_atual}", inline=True)
        embed.add_field(name="✨ XP Atual", value=f"{xp_atual} XP", inline=True)
        embed.add_field(name="🥇 Colocação", value=f"#{posicao}", inline=True)
        embed.add_field(name="📈 XP pro próximo nível", value=f"{xp_faltando} XP", inline=True)
        if proximo_cargo:
            embed.add_field(name="🎁 Próxima recompensa", value=proximo_cargo, inline=True)
        await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(XP(bot))