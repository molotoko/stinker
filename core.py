import random
import telebot
import requests
import lxml.html as html
import unicodedata
from config import telegram_api_key

bot = telebot.TeleBot(telegram_api_key)


@bot.message_handler(commands=['ow'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        'Го в Overwatch! @MoshWayne @mikmall @molotoko @Milli_M @Valion @HKEY47 @fyvdlo @bddah @B1oodB1ade @S1aaneesh',
        parse_mode='Markdown',
    )


bot.polling()
