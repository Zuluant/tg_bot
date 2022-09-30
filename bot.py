import telebot
import lessons
from datetime import datetime
from telebot import types

bot = telebot.TeleBot('5799245966:AAEy8F_GkpAqXr9la3FiZaXv17EK1n9DhyE')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} введите /help'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_help = types.KeyboardButton('/help')
    markup.add(button_help)
    bot.send_message(message.chat.id, mess, reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    mess = f'В этом боте можно узнать какой будет следующий урок, а также получить на него код и ссылку.' \
           f'Внимание! Бот не предоставляет ссылок на конференции для первой группы, а также не даёт ссылки' \
           f' на чередующиеся уроки'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    what_lesson_now = types.KeyboardButton('/lesson')
    markup.add(what_lesson_now)
    bot.send_message(message.chat.id, mess, reply_markup=markup)


@bot.message_handler(commands=['lesson'])
def lesson(message):
    current_time = int(datetime.now().strftime('%H%M'))
    day = datetime.now().strftime('%A')
    bot.send_message(message.chat.id, lessons.what_is_lesson_now(day, current_time))


bot.polling(none_stop=True)
