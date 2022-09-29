import telebot
from datetime import datetime


# bot = telebot.TeleBot('5799245966:AAErU-lQCZaTDXHDspDaMzINoe2mir6CBAc')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess)


@bot.message_handler()
def get_user_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, 'И тебе привет!')
    elif message.text.lower() == 'photo':
        photo = open('1.webp', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text.lower() == 'time':
        bot.send_message(message.chat.id, datetime.now())
    else:
        bot.send_message(message.chat.id, f'Я тебя не понимаю')


bot.polling(none_stop=True)
