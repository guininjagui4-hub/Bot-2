import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from datetime import datetime

# Carrega variáveis de ambiente
load_dotenv()

# Configuração do bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

# Sincronizar comandos slash
@bot.event
async def on_ready():
    """Evento quando o bot está pronto"""
    try:
        synced = await bot.tree.sync()
        print(f'✅ Bot {bot.user} conectado com sucesso!')
        print(f'📋 {len(synced)} comandos sincronizados')
    except Exception as e:
        print(f'❌ Erro ao sincronizar comandos: {e}')
    
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Dúvidas?"))
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Assina aqui tio paulo"))
# Token do Discord
TOKEN = os.getenv('DISCORD_TOKEN')

# Cores personalizadas
NIKITO_PINK = 0xFF1493  # Rosa do Nikito
NIKITO_PURPLE = 0x9932CC  # Roxo

# Mensagens do bot (estilo Nikito)
NIKITO_RESPONSES = {
    "falar": [
        "Oi querido! Tá tudo bem com você? 😜",
        "Hehe, achei legal você chamar! O que você quer?",
        "Opa opa! Já chegou o Nikito! 💕",
        "Que legal! Sempre bom conversar!",
        "Oi babe! 😘 Tá pensando em mim?",
        "E aí, tudo certo? Quer bater um papo? 😎",
       "assina aqui tio paulo"
      ],
    "avatar": [
        "Aqui está meu rosto mais lindo! 💋",
        "É... EU! Bonita né? 💕",
        "Meu avatar favorito! Fofucho demais!",
    ],
}

@bot.tree.command(name='falar', description='Nikito fala para você!')
async def falar(interaction: discord.Interaction):
    """Comando /falar - Nikito responde com uma mensagem divertida"""
    import random
    
    embed = discord.Embed(
        title="💕 Oi! É o Nikito aqui!",
        description=random.choice(NIKITO_RESPONSES["falar"]),
        color=NIKITO_PINK,
        timestamp=datetime.now()
    )
    
    embed.set_author(name="Nikito", icon_url=bot.user.avatar.url if bot.user.avatar else None)
    embed.set_footer(text=f"Pedido por {interaction.user.name}", icon_url=interaction.user.avatar.url if interaction.user.avatar else None)
    embed.add_field(name="Status", value="✨ Pronto para conversar! ✨", inline=False)
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name='avatar', description='Veja o avatar do Nikito!')
async def avatar(interaction: discord.Interaction):
    """Comando /avatar - Mostra o avatar do bot"""
    import random
    
    embed = discord.Embed(
        title="🖼️ Meu Avatar!",
        description=random.choice(NIKITO_RESPONSES["avatar"]),
        color=NIKITO_PURPLE,
        timestamp=datetime.now()
    )
    
    if bot.user.avatar:
        embed.set_image(url=bot.user.avatar.url)
    
    embed.set_author(name="Nikito", icon_url=bot.user.avatar.url if bot.user.avatar else None)
    embed.set_footer(text=f"Pedido por {interaction.user.name}", icon_url=interaction.user.avatar.url if interaction.user.avatar else None)
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name='status', description='Muda meu status!')
@app_commands.describe(status_text="Novo status para o bot")
async def status(interaction: discord.Interaction, status_text: str = "vivendo a melhor vida! 💕"):
    """Comando /status - Muda o status do bot"""
    
    embed = discord.Embed(
        title="📊 Status Atualizado!",
        description=f"Agora estou: **{status_text}**",
        color=NIKITO_PINK,
        timestamp=datetime.now()
    )
    
    embed.set_author(name="Nikito", icon_url=bot.user.avatar.url if bot.user.avatar else None)
    embed.add_field(name="👤 Atualizado por", value=interaction.user.name, inline=True)
    embed.set_footer(text="Status mudou com sucesso!", icon_url=interaction.user.avatar.url if interaction.user.avatar else None)
    
    # Muda o status do bot
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status_text))
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name='info', description='Informações sobre o Nikito!')
async def info(interaction: discord.Interaction):
    """Comando /info - Mostra informações sobre o bot"""
    
    embed = discord.Embed(
        title="💖 Sobre o Nikito",
        description="Oi! Eu sou o Nikito, seu bot favorito! 🎀",
        color=NIKITO_PINK,
        timestamp=datetime.now()
    )
    
    embed.add_field(name="📝 Nome", value="Nikito", inline=True)
    embed.add_field(name="💕 Personalidade", value="Divertido e sarcástico", inline=True)
    embed.add_field(name="🎯 Missão", value="Animar seu servidor!", inline=True)
    embed.add_field(name="📢 Comandos", value="`/falar` • `/avatar` • `/status` • `/info`", inline=False)
    
    embed.set_author(name="Nikito", icon_url=bot.user.avatar.url if bot.user.avatar else None)
    embed.set_footer(text=f"Pedido por {interaction.user.name}", icon_url=interaction.user.avatar.url if interaction.user.avatar else None)
    
    await interaction.response.send_message(embed=embed)

@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    """Trata erros de comando"""
    
    embed = discord.Embed(
        title="❌ Opa! Tive um probleminha!",
        description=f"Erro: `{type(error).__name__}`",
        color=discord.Color.red(),
        timestamp=datetime.now()
    )
    
    embed.add_field(name="📝 Detalhes", value=str(error)[:1024], inline=False)
    embed.set_footer(text="Me desculpa! 😅")
    
    await interaction.response.send_message(embed=embed)

# Inicia o bot
if __name__ == "__main__":
    bot.run(TOKEN)
