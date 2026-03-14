import discord
from discord.ext import commands

class Comandos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    async def embed_regras(self, ctx:commands.Context):
        regras_intro = discord.Embed()
        regras_intro.title = "<:rize_coffe:1477833497434656819>  **|** 🎀 Combinados da Comunidade\n\n"
        regras_intro.description = (
            " Para manter o servidor organizado, seguro e agradável para todos, pedimos que leia atentamente as regras abaixo.\n\n"
            "Lembre-se: Ao permanecer no servidor, você concorda com nossas diretrizes e com as orientações da equipe de moderação.\n"
        )
        regras_intro.set_footer(text="As regras podem ser atualizadas pela staff sempre que necessário.")

        regras_convi = discord.Embed()
        regras_convi.title = "<:rize_coffe:1477833497434656819>  **|** Convivência\n\n"
        regras_convi.description = (
            "• Respeite todos os membros do servidor.\n"
            "• Evite discussões agressivas, provocações ou brigas desnecessárias.\n"
            "• Problemas pessoais devem ser resolvidos em mensagens privadas (DM), não no chat público.\n"
            "• Não tente provocar punições em outros membros ou criar situações para prejudicar alguém.\n"
            "• A equipe de moderação tem a palavra final em decisões relacionadas ao servidor.\n"
        )

        regras_chat = discord.Embed()
        regras_chat.title = "<:rize_coffe:1477833497434656819>  **|** Chats e Comportamento"
        regras_chat.description = (
            "• Evite spam, flood ou envio de mensagens repetitivas nos chats.\n"
            "• Não faça spam de microfone, áudio ou soundboard nos canais de voz.\n"
            "• Evite ping excessivo ou menções em massa sem necessidade.\n"
            "• Publicidade, divulgação de servidores ou projetos só é permitida com autorização da staff.\n"
        )

        regras_seg = discord.Embed()
        regras_seg.title = "<:rize_coffe:1477833497434656819>  **|** Segurança e Conteúdo"
        regras_seg.description = (
            "• Não envie links suspeitos, maliciosos ou conteúdos enganosos.\n"
            "• Conteúdos gore, NSFW ou pornográficos não são permitidos no servidor.\n"
            "• Qualquer forma de preconceito, assédio ou comportamento ofensivo não será tolerado.\n"
            "• Não utilize contas alternativas para burlar regras ou punições.\n"
            "• Em casos de infração, a punição pode variar entre aviso, timeout ou banimento dependendo da gravidade."
        )

        await ctx.send(embeds=[regras_intro, regras_convi, regras_chat, regras_seg])

    @commands.command()
    async def ola(self, ctx:commands.Context):
        nome = ctx.author.name
        await ctx.reply(f"Olá, {nome}! Tudo bem?")


    @commands.command()
    async def boanoite(self, ctx:commands.Context):
        nome = ctx.author.name
        await ctx.reply(f"Boa noiteeee {nome}!")

async def setup(bot):
    await bot.add_cog(Comandos(bot))