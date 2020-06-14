import telebot
from telebot.apihelper import ApiException

import json

# from settings import telegram_api_key
from config import telegram_api_key

bot = telebot.TeleBot(telegram_api_key)
jekpot_id = 809456
testers = [60383050, 162165102]
overwatchers = [60383050, 162165102, 123085544, 37718983, 224502157, 144235785, 145375898, 246713426, 658658324]


@bot.message_handler(commands=['ow'])
def call_overwatchers(message):
    caller_id = message.from_user.id
    if caller_id != jekpot_id:
        chat_id = message.chat.id
        first_message = 'Го в Overwatch! Призываю @molotoko @mikmall @S1aaneesh @fyvdlo'
        second_message = 'Также в Overwatch призываются @B1oodB1ade @Valion @nogpyra @bddah'
        third_message = 'Погнали гореть в Overwatch! @kokos_89 @MoshWayne @sslippe @OctLeaf @Milli_M'
        bot.send_message(
            chat_id,
            first_message
        )
        bot.send_message(
            chat_id,
            second_message
        )
        bot.send_message(
            chat_id,
            third_message
        )
    else:
        bot.send_message(
            message.chat.id,
            'Sorry, you cannot do it.',
            reply_to_message_id=message.message_id
        )


@bot.message_handler(commands=['dota'])
def call_doters(message):
    chat_id = message.chat.id
    message = '@wilddeer @JekPot @Milli_M @Ap4u121 @nogpyra @sslippe @fyvdlo go zaebali'
    bot.send_message(
        chat_id,
        message
    )


@bot.message_handler(commands=['dimon'])
def call_doters(message):
    chat_id = message.chat.id
    message = '@tsynali где Димон?'
    bot.send_message(
        chat_id,
        message
    )


def extract_arg(arg):
    return arg.split()[1:]


@bot.message_handler(commands=['page'])
def add_page(message):
    caller_id = message.from_user.id
    if caller_id != jekpot_id:
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
        tmp_msg = f'Lizavetka has already read pages: {read_pages}.'
        bot.send_message(
            message.chat.id,
            'Sorry, this command is not working.',
            parse_mode='Markdown'
        )


# random Liza's picture


bot.polling()
