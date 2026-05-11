import os
import telebot

TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def reply(msg):
    bot.reply_to(msg, "Hello! I'm alive 🤖")

print("Bot started polling...")
bot.infinity_polling()
