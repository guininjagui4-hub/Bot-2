# 🛠️ Guia PM2 - Rodar Bot 24 Horas

## O que é PM2?

PM2 é um gerenciador de processos que mantém sua aplicação rodando 24/7, com restart automático em caso de crash.

## 📦 Instalação

### 1. Instalar Node.js (necessário para PM2)
- Windows: [nodejs.org](https://nodejs.org)
- Linux: `sudo apt install nodejs npm`
- macOS: `brew install node`

### 2. Instalar PM2
```bash
npm install -g pm2
```

## 🚀 Como usar

### Windows
1. Duplo clique em `start-pm2.bat`
2. Aguarde a instalação completar
3. Pronto! Bot rodando 24/7

### Linux/Mac
```bash
chmod +x start-pm2.sh
./start-pm2.sh
```

Ou manualmente:
```bash
npm install -g pm2
pip install -r requirements.txt
pm2 start ecosystem.config.js
pm2 save
pm2 startup
```

## 📋 Comandos PM2

### Ver status
```bash
pm2 status
pm2 monit  # Monitor em tempo real
```

### Ver logs
```bash
pm2 logs harley-bot           # Todos os logs
pm2 logs harley-bot --lines 50  # Últimas 50 linhas
pm2 logs harley-bot --err     # Apenas erros
```

### Controlar o bot
```bash
pm2 restart harley-bot  # Reiniciar
pm2 stop harley-bot     # Parar temporariamente
pm2 start harley-bot    # Iniciar
pm2 delete harley-bot   # Remover do PM2
```

### Auto-iniciar na boot
```bash
pm2 startup      # Gerar comando de inicialização
pm2 save         # Salvar configuração
```

## 📊 Monitoramento

### Dashboard web
```bash
pm2 web
```
Acesse: http://localhost:9615

### Logs em tempo real
```bash
pm2 logs harley-bot
```

## 🔍 Troubleshooting

**Bot não inicia?**
```bash
pm2 logs harley-bot --err  # Ver erro
pm2 delete harley-bot      # Remover
pm2 start ecosystem.config.js  # Reiniciar
```

**Verificar se Python está instalado**
```bash
python --version
pip --version
```

**Limpar cache PM2**
```bash
pm2 kill
pm2 start ecosystem.config.js
```

## 📈 Configurações personalizadas

Edite `ecosystem.config.js` para:
- `max_memory_restart` - Reiniciar se usar mais de 500MB
- `autorestart` - Auto-restart em caso de crash
- `max_restarts` - Máximo de restarts antes de parar
- `watch` - Monitorar mudanças de arquivo

## 🎯 Resumo

| O que você quer | Comando |
|---|---|
| Iniciar o bot | `pm2 start ecosystem.config.js` |
| Ver status | `pm2 status` |
| Ver logs | `pm2 logs harley-bot` |
| Parar | `pm2 stop harley-bot` |
| Reiniciar | `pm2 restart harley-bot` |
| Auto-iniciar na boot | `pm2 startup && pm2 save` |

---

**Seu bot rodando 24/7! 💕**
