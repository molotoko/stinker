import telebot

import json

# from settings import telegram_api_key
from config import telegram_api_key

bot = telebot.TeleBot(telegram_api_key)
jekpot_id = 809456


@bot.message_handler(commands=['ow'])
def call_overwatchers(message):
    user_id = message.from_user.id
    if user_id != jekpot_id:
        chat_id = message.chat.id
        # testers = [60383050, 162165102]
        ow_caller = f'Го в Overwatch! Призываю '
        overwatchers = [60383050, 162165102, 123085544, 37718983, 224502157, 144235785, 145375898, 246713426, 658658324]
        for user_id in overwatchers:
            user_info = bot.get_chat_member(chat_id, user_id).__dict__
            username = user_info['user'].__dict__['username']
            ow_caller += f'@{username} '

        bot.send_message(
            chat_id,
            ow_caller,
            parse_mode='Markdown'
        )
    else:
        bot.send_message(
            message.chat.id,
            f'Sorry, you cannot do it.',
            parse_mode='Markdown'
        )


def extract_arg(arg):
    return arg.split()[1:]


@bot.message_handler(commands=['page'])
def add_page(message):
    user_id = message.from_user.id
    if user_id != jekpot_id:
        query_pages_text = extract_arg(message.text)
        query_pages = []
        for page in query_pages_text:
            query_pages.append(int(page))

        with open('data.txt', 'r+') as data_file:
            data_dict = json.load(data_file)
            read_pages = data_dict['pages']

            for page in query_pages:
                if page not in read_pages:
                    read_pages.append(page)
                    bot.send_message(
                        message.chat.id,
                        f'A page number {page} has been added to the list.',
                        parse_mode='Markdown'
                    )
                else:
                    bot.send_message(
                        message.chat.id,
                        f'The list already has a page number {page}.',
                        parse_mode='Markdown'
                    )

            data_file.seek(0)  # rewind
            json.dump(dict(pages=read_pages), data_file)
            data_file.truncate()
            data_file.close()
    else:
        bot.send_message(
            message.chat.id,
            f'Sorry, you cannot do it.',
            parse_mode='Markdown'
        )


@bot.message_handler(commands=['pages'])
def all_pages(message):
    with open('data.txt', 'r') as data_file:
        data_dict = json.load(data_file)
        read_pages = sorted(data_dict['pages'])
        bot.send_message(
            message.chat.id,
            f'Lizavetka has already read pages: {read_pages}.',
            parse_mode='Markdown'
        )


# random Liza's picture


bot.polling()
