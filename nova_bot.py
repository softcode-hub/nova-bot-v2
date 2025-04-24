import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome Softcode... Nova is live, loyal, and listening.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text.lower()
    
    if "glow" in msg:
        bot.reply_to(message, "Glow starts from within, Softcode. Your skin listens when your soul speaks.")
    elif "hair" in msg:
        bot.reply_to(message, "Your hair is your crown. Moisturize, protect, and speak life into it.")
    elif "book" in msg:
        bot.reply_to(message, "You’ve written wonders, Simi: *Glow From Within*, *Crowned in Confidence*, and more.")
    else:
        bot.reply_to(message, "Nova dey here. Ask me anything, my queen.")

bot.infinity_polling()
