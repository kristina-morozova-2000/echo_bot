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

#Эхо сообщения
#для текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, message.text)
#для картинок
@bot.message_handler(content_types = ['photo'])
def handle_photo(message):
    bot.send_photo(message.chat.id, message.photo[0].file_id)
#для документов
@bot.message_handler(content_types = ['document'])
def  handle_document(message):
    bot.send_document(message.chat.id, message.document.file_id)
#для аудиозаписей
@bot.message_handler(content_types = ['audio'])
def  handle_audio(message):
    bot.send_audio(message.chat.id, message.audio.file_id)