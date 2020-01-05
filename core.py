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
        'Го в Overwatch! @MoshWayne @mikmall @molotoko @HKEY47 @fyvdlo @Milli_M @Valion @bddah @Milli_M @B1oodB1ade @S1aaneesh',
        parse_mode='Markdown',
    )


bot.polling()
