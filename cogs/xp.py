import discord
from discord.ext import commands
import random
from database import conectar

class XP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
        self.cooldowns = {}

    @commands.Cog.listener()
    async def on_message(self, mensagem:discord.Message):
        if mensagem.author.bot:
            return
        if mensagem.guild is None:  # ignora DMs
            return
        import time
        agora = time.time()
        usuario_id = mensagem.author.id
        servidor_id = mensagem.guild.id

        ultimo = self.cooldowns.get(usuario_id, 0)
        if agora - ultimo < 60:
            return
        
        self.cooldowns[usuario_id] = agora

        xp_ganho = random.randint(15, 25)
        
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

        cursor.execute("""
            SELECT xp, nivel FROM xp
            WHERE usuario_id = %s AND servidor_id = %s
        """, (usuario_id, servidor_id))
        
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()

        if resultado:
            xp_atual, nivel_atual = resultado
            xp_necessario = nivel_atual * 100
            
            if xp_atual >= xp_necessario:
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
                await mensagem.channel.send(
                    f"🎉 {mensagem.author.mention} subiu para o **nível {novo_nivel}**!"
                )

async def setup(bot):
    await bot.add_cog(XP(bot))