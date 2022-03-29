import telebot
import os
from dotenv import load_dotenv

#Экземпляр бота
load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN_BOT'))

#Сообщение-приветствие
@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я - эхо-бот. Напиши что-нибудь, и я это повторю.')