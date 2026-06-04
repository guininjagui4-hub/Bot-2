@echo off
REM 📦 Script para rodar o bot com PM2 (24 horas) - Windows

echo 🚀 Iniciando Harley Bot com PM2...

REM Instalar PM2 globalmente (se não tiver)
echo Instalando PM2...
npm install -g pm2

REM Instalar dependências Python
echo Instalando dependências Python...
pip install -r requirements.txt

REM Criar pasta de logs
if not exist logs mkdir logs

REM Iniciar com PM2
echo Iniciando bot com PM2...
pm2 start ecosystem.config.js

REM Salvar configuração PM2
pm2 save
pm2 startup

echo.
echo ✅ Bot iniciado com PM2!
echo.
echo 📋 Comandos úteis:
echo   pm2 status              - Ver status do bot
echo   pm2 logs harley-bot     - Ver logs em tempo real
echo   pm2 restart harley-bot  - Reiniciar o bot
echo   pm2 stop harley-bot     - Parar o bot
echo   pm2 delete harley-bot   - Remover do PM2
echo.
echo 💾 Para o bot iniciar automaticamente ao ligar a máquina:
echo   pm2 startup
echo.
pause
