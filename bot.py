import telebot
from datetime import datetime
from telebot import types


bot = telebot.TeleBot('5799245966:AAEy8F_GkpAqXr9la3FiZaXv17EK1n9DhyE')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} введите /help'
    markup = types.ReplyKeyboardMarkup()
    button_help = types.KeyboardButton('/help')
    markup.add(button_help)
    bot.send_message(message.chat.id, mess, reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    mess = f'В этом боте можно узнать какой будет следующий урок, а также получить на него код и ссылку.'
    bot.send_message(message.chat.id, mess)


@bot.message_handler(commands=['lesson'])
def lesson(message):
    current_time = datetime.now().strftime('%H:%M:%S')
    if current_time == '00:46:40':
        bot.send_message(message.chat.id, 'Сейчас будет биология!')
    bot.send_message(message.chat.id, current_time)


bot.polling(none_stop=True)
