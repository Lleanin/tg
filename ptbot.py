import ptbot

TG_TOKEN = '5940854841:AAHiH3vpipCe1I3k3AbqpDeL4QuJIGXK0Q4'  # подставьте свой ключ API
TG_CHAT_ID = '974988251'  # подставьте свой ID
bot = ptbot.Bot(TG_TOKEN)
bot.send_message(TG_CHAT_ID, "Бот запущен")
bot.run_bot()