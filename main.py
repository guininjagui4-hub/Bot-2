import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime

# Carrega variáveis de ambiente
load_dotenv()

# Configuração do bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

# Token do Discord
TOKEN = os.getenv('DISCORD_TOKEN')

# Cores personalizadas
HARLEY_PINK = 0xFF1493  # Rosa da Harley
HARLEY_PURPLE = 0x9932CC  # Roxo

# Mensagens do bot (estilo Harley Clark)
HARLEY_RESPONSES = {
    "falar": [
        "Oi querido! Tá tudo bem com você? 😜",
        "Hehe, achei legal você chamar! O que você quer?",
        "Opa opa! Já chegou a Harley! 💕",
        "Que legal! Sempre bom conversar!",
        "Oi babe! 😘 Tá pensando em mim?",
    ],
    "avatar": [
        "Aqui está meu rosto mais lindo! 💋",
        "É... EU! Bonita né? 💕",
        "Meu avatar favorito! Fofucho demais!",
    ],
}

@bot.event
async def on_ready():
    """Evento quando o bot está pronto"""
    print(f'✅ Bot {bot.user} conectado com sucesso!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="você"))

@bot.command(name='falar', description='Harley fala para você!')
async def falar(ctx):
    """Comando /falar - Harley responde com uma mensagem divertida"""
    import random
    
    embed = discord.Embed(
        title="💕 Oi! É a Harley aqui!",
        description=random.choice(HARLEY_RESPONSES["falar"]),
        color=HARLEY_PINK,
        timestamp=datetime.now()
    )
    
    embed.set_author(name="Harley Clark", icon_url=bot.user.avatar.url if bot.user.avatar else None)
    embed.set_footer(text=f"Pedido por {ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
    embed.add_field(name="Status", value="✨ Pronta para conversar! ✨", inline=False)
    
    await ctx.send(embed=embed)

@bot.command(name='avatar', description='Veja o avatar da Harley!')
async def avatar(ctx):
    """Comando /avatar - Mostra o avatar do bot"""
    import random
    
    embed = discord.Embed(
        title="🖼️ Meu Avatar!",
        description=random.choice(HARLEY_RESPONSES["avatar"]),
        color=HARLEY_PURPLE,
        timestamp=datetime.now()
    )
    
    if bot.user.avatar:
        embed.set_image(url=bot.user.avatar.url)
    
    embed.set_author(name="Harley Clark", icon_url=bot.user.avatar.url if bot.user.avatar else None)
    embed.set_footer(text=f"Pedido por {ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
    
    await ctx.send(embed=embed)

@bot.command(name='status', description='Muda meu status!')
async def status(ctx, *, status_text=None):
    """Comando /status - Muda o status do bot"""
    
    if not status_text:
        status_text = "vivendo a melhor vida! 💕"
    
    embed = discord.Embed(
        title="📊 Status Atualizado!",
        description=f"Agora estou: **{status_text}**",
        color=HARLEY_PINK,
        timestamp=datetime.now()
    )
    
    embed.set_author(name="Harley Clark", icon_url=bot.user.avatar.url if bot.user.avatar else None)
    embed.add_field(name="👤 Atualizado por", value=ctx.author.name, inline=True)
    embed.set_footer(text="Status mudou com sucesso!", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
    
    # Muda o status do bot
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status_text))
    
    await ctx.send(embed=embed)

@bot.command(name='info', description='Informações sobre a Harley!')
async def info(ctx):
    """Comando /info - Mostra informações sobre o bot"""
    
    embed = discord.Embed(
        title="💖 Sobre a Harley",
        description="Oi! Eu sou a Harley Clark, seu bot favorito! 🎀",
        color=HARLEY_PINK,
        timestamp=datetime.now()
    )
    
    embed.add_field(name="📝 Nome", value="Harley Clark", inline=True)
    embed.add_field(name="💕 Personalidade", value="Divertida e sarcástica", inline=True)
    embed.add_field(name="🎯 Missão", value="Animar seu servidor!", inline=True)
    embed.add_field(name="📢 Comandos", value="`/falar` • `/avatar` • `/status` • `/info`", inline=False)
    
    embed.set_author(name="Harley Clark", icon_url=bot.user.avatar.url if bot.user.avatar else None)
    embed.set_footer(text=f"Pedido por {ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
    
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    """Trata erros de comando"""
    
    embed = discord.Embed(
        title="❌ Opa! Tive um probleminha!",
        description=f"Erro: `{type(error).__name__}`",
        color=discord.Color.red(),
        timestamp=datetime.now()
    )
    
    embed.add_field(name="📝 Detalhes", value=str(error)[:1024], inline=False)
    embed.set_footer(text="Me desculpa! 😅")
    
    await ctx.send(embed=embed)

# Inicia o bot
if __name__ == "__main__":
    bot.run(TOKEN)
