import os
import random
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from datetime import datetime

# Carrega variáveis de ambiente (funciona local, ignorado no Railway)
load_dotenv()

# Configuração do bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

# Cores personalizadas
NIKITO_PINK   = 0xFF1493
NIKITO_PURPLE = 0x9932CC

# Mensagens do bot (estilo Nikito)
NIKITO_RESPONSES = {
    "falar": [
        "Oi querido! Tá tudo bem com você? 😜",
        "Hehe, achei legal você chamar! O que você quer?",
        "Opa opa! Já chegou o Nikito! 💕",
        "Que legal! Sempre bom conversar!",
        "Oi babe! 😘 Tá pensando em mim?",
        "E aí, tudo certo? Quer bater um papo? 😎",
        "assina aqui tio paulo",
    ],
    "avatar": [
        "Aqui está meu rosto mais lindo! 💋",
        "É... EU! Bonita né? 💕",
        "Meu avatar favorito! Fofucho demais!",
    ],
}

# Helpers para evitar crash quando avatar é None
def bot_avatar_url():
    return bot.user.avatar.url if bot.user and bot.user.avatar else None

def user_avatar_url(user: discord.User | discord.Member):
    return user.avatar.url if user.avatar else None


# ──────────────────────────────────────────
# Eventos
# ──────────────────────────────────────────

@bot.event
async def on_ready():
    """Evento quando o bot está pronto"""
    try:
        synced = await bot.tree.sync()
        print(f'✅ Bot {bot.user} conectado com sucesso!')
        print(f'📋 {len(synced)} comandos sincronizados')
    except Exception as e:
        print(f'❌ Erro ao sincronizar comandos: {e}')

    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="Dúvidas?")
    )


# ──────────────────────────────────────────
# Comandos Slash
# ──────────────────────────────────────────

@bot.tree.command(name='falar', description='Nikito fala para você!')
async def falar(interaction: discord.Interaction):
    """Comando /falar – Nikito responde com uma mensagem divertida"""
    embed = discord.Embed(
        title="💕 Oi! É o Nikito aqui!",
        description=random.choice(NIKITO_RESPONSES["falar"]),
        color=NIKITO_PINK,
        timestamp=datetime.now(),
    )
    embed.set_author(name="Nikito", icon_url=bot_avatar_url())
    embed.set_footer(
        text=f"Pedido por {interaction.user.name}",
        icon_url=user_avatar_url(interaction.user),
    )
    embed.add_field(name="Status", value="✨ Pronto para conversar! ✨", inline=False)

    await interaction.response.send_message(embed=embed)


@bot.tree.command(name='avatar', description='Veja o avatar do Nikito!')
async def avatar(interaction: discord.Interaction):
    """Comando /avatar – Mostra o avatar do bot"""
    embed = discord.Embed(
        title="🖼️ Meu Avatar!",
        description=random.choice(NIKITO_RESPONSES["avatar"]),
        color=NIKITO_PURPLE,
        timestamp=datetime.now(),
    )
    if bot.user and bot.user.avatar:
        embed.set_image(url=bot.user.avatar.url)

    embed.set_author(name="Nikito", icon_url=bot_avatar_url())
    embed.set_footer(
        text=f"Pedido por {interaction.user.name}",
        icon_url=user_avatar_url(interaction.user),
    )

    await interaction.response.send_message(embed=embed)


@bot.tree.command(name='status', description='Muda meu status!')
@app_commands.describe(status_text="Novo status para o bot")
async def status(
    interaction: discord.Interaction,
    status_text: str = "vivendo a melhor vida! 💕",
):
    """Comando /status – Muda o status do bot"""
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name=status_text)
    )

    embed = discord.Embed(
        title="📊 Status Atualizado!",
        description=f"Agora estou: **{status_text}**",
        color=NIKITO_PINK,
        timestamp=datetime.now(),
    )
    embed.set_author(name="Nikito", icon_url=bot_avatar_url())
    embed.add_field(name="👤 Atualizado por", value=interaction.user.name, inline=True)
    embed.set_footer(
        text="Status mudou com sucesso!",
        icon_url=user_avatar_url(interaction.user),
    )

    await interaction.response.send_message(embed=embed)


@bot.tree.command(name='info', description='Informações sobre o Nikito!')
async def info(interaction: discord.Interaction):
    """Comando /info – Mostra informações sobre o bot"""
    embed = discord.Embed(
        title="💖 Sobre o Nikito",
        description="Oi! Eu sou o Nikito, seu bot favorito! 🎀",
        color=NIKITO_PINK,
        timestamp=datetime.now(),
    )
    embed.add_field(name="📝 Nome",        value="Nikito",                  inline=True)
    embed.add_field(name="💕 Personalidade", value="Divertido e sarcástico", inline=True)
    embed.add_field(name="🎯 Missão",      value="Animar seu servidor!",    inline=True)
    embed.add_field(
        name="📢 Comandos",
        value="`/falar` • `/avatar` • `/status` • `/info`",
        inline=False,
    )
    embed.set_author(name="Nikito", icon_url=bot_avatar_url())
    embed.set_footer(
        text=f"Pedido por {interaction.user.name}",
        icon_url=user_avatar_url(interaction.user),
    )

    await interaction.response.send_message(embed=embed)


# ──────────────────────────────────────────
# Tratamento de erros
# ──────────────────────────────────────────

@bot.tree.error
async def on_app_command_error(
    interaction: discord.Interaction,
    error: app_commands.AppCommandError,
):
    embed = discord.Embed(
        title="❌ Opa! Tive um probleminha!",
        description=f"Erro: `{type(error).__name__}`",
        color=discord.Color.red(),
        timestamp=datetime.now(),
    )
    embed.add_field(name="📝 Detalhes", value=str(error)[:1024], inline=False)
    embed.set_footer(text="Me desculpa! 😅")

    # Verifica se já respondemos antes de tentar responder de novo
    if interaction.response.is_done():
        await interaction.followup.send(embed=embed, ephemeral=True)
    else:
        await interaction.response.send_message(embed=embed, ephemeral=True)


# ──────────────────────────────────────────
# Start
# ──────────────────────────────────────────

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")

    if not TOKEN:
        raise ValueError("❌ DISCORD_TOKEN não encontrado! Adicione a variável no Railway.")

    bot.run(TOKEN)