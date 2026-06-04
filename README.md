# 💕 Harley Clark Bot

Bot Discord com personalidade sarcástica e divertida, estilo Harley Clark! Responde todos os comandos com embeds bonitos e personalizados.

## 🎯 Funcionalidades

- **`/falar`** - Harley responde com mensagens divertidas em embed
- **`/avatar`** - Mostra o avatar bonito da Harley
- **`/status`** - Muda o status do bot dinamicamente
- **`/info`** - Informações sobre a Harley

## 🚀 Instalação

### Pré-requisitos
- Python 3.8+
- Token de Bot Discord

### Passos

1. **Clone ou copie o projeto:**
```bash
cd seu-diretorio
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Configure o arquivo `.env`:**
```bash
cp .env.example .env
```

Edite o `.env` e adicione seu token:
```
DISCORD_TOKEN=seu_token_discord_aqui
```

5. **Execute o bot:**
```bash
python main.py
```

## 🤖 Rodar 24 Horas com PM2

Para deixar seu bot rodando 24/7 mesmo que você desligue o PC:

### Windows
1. Duplo clique em `start-pm2.bat`
2. Aguarde a instalação completar
3. Bot iniciado! ✅

### Linux/Mac
```bash
chmod +x start-pm2.sh
./start-pm2.sh
```

Ou manualmente:
```bash
npm install -g pm2
pm2 start ecosystem.config.js
pm2 save
pm2 startup
```

### Comandos úteis PM2
```bash
pm2 status           # Ver status do bot
pm2 logs harley-bot  # Ver logs em tempo real
pm2 restart harley-bot  # Reiniciar o bot
pm2 stop harley-bot  # Parar o bot
```

👉 Veja [PM2-GUIDE.md](PM2-GUIDE.md) para mais detalhes!

## 📦 Deploy no Railway

### 1. Prepare o repositório
```bash
git init
git add .
git commit -m "Initial commit"
```

### 2. No Railway
- Acesse [railway.app](https://railway.app)
- Clique em "New Project"
- Escolha "Deploy from GitHub" (ou upload o código)
- Selecione o repositório

### 3. Configure variáveis de ambiente
No dashboard do Railway:
- Clique em "Variables"
- Adicione: `DISCORD_TOKEN=seu_token_aqui`

### 4. Deploy
- O bot iniciará automaticamente!

## 🤖 Como criar um Bot Discord

1. Vá para [Discord Developer Portal](https://discord.com/developers/applications)
2. Clique em "New Application"
3. Nome: "Harley Clark"
4. Vá para "Bot" → "Add Bot"
5. Em "TOKEN", clique em "Copy"
6. Cole o token no `.env`

### Permissões necessárias
- Send Messages
- Embed Links
- Read Messages/View Channels

## 📝 Customização

### Mudar cores
No `main.py`, altere as variáveis:
```python
HARLEY_PINK = 0xFF1493
HARLEY_PURPLE = 0x9932CC
```

### Adicionar respostas
Adicione mais opções em `HARLEY_RESPONSES`:
```python
HARLEY_RESPONSES = {
    "falar": [
        "Sua mensagem aqui!",
        "Outra mensagem!",
    ]
}
```

## 🆘 Troubleshooting

**Bot não aparece online?**
- Verifique o token no `.env`
- Reinicie o bot

**Embeds não aparecem?**
- Verifique as permissões do bot no servidor
- Certifique-se que "Embed Links" está habilitado

**Comandos não funcionam?**
- Use `/` no Discord para ativar os comandos slash
- Aguarde 1 minuto para sync dos comandos

## 📄 Licença

Livre para usar e modificar! 💕

---

**Feito com ❤️ para seu amigo**
