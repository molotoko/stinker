import random
import telebot
import requests
import lxml.html as html
import unicodedata
from config import telegram_api_key

bot = telebot.TeleBot(telegram_api_key)


@bot.message_handler(commands=['ow'])
def start_message(message):
    bot.send_message(message.chat.id, 'Го в Overwatch! @MoshWayne @molotoko @mikmall @HKEY47 @fyvdlo @Valion @bddah '
                                      '@Milli_M @B1oodB1ade @S1aaneesh')


bot.polling()
