import telebot
import os
from dotenv import load_dotenv

#Экземпляр бота
load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN_BOT'))