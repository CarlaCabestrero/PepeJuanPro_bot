import os
import telebot
  
bot = telebot.TeleBot(os.environ['PEPEJUANBOT_API_TOKEN'])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u"Holii soy Pepe Juan")
    


bot.polling()
