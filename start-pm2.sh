#!/bin/bash

# 📦 Script para rodar o bot com PM2 (24 horas)

echo "🚀 Iniciando Harley Bot com PM2..."

# Instalar PM2 globalmente (se não tiver)
npm install -g pm2

# Instalar dependências Python
pip install -r requirements.txt

# Iniciar com PM2
pm2 start ecosystem.config.js

# Salvar configuração PM2 para iniciar automaticamente
pm2 save
pm2 startup

echo "✅ Bot iniciado com PM2!"
echo ""
echo "📋 Comandos úteis:"
echo "  pm2 status              - Ver status do bot"
echo "  pm2 logs harley-bot     - Ver logs em tempo real"
echo "  pm2 restart harley-bot  - Reiniciar o bot"
echo "  pm2 stop harley-bot     - Parar o bot"
echo "  pm2 delete harley-bot   - Remover do PM2"
echo ""
echo "💾 Para o bot iniciar automaticamente ao ligar a máquina:"
echo "  pm2 startup"
