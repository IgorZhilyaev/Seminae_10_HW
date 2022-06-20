import telebot
from telebot import types

TOKEN = "5455158181:AAHS2F7oZM-Shb3wiGWUNjTs7hl6vDwc6sU"
bot = telebot.TeleBot(TOKEN)

value = ''
old_value = ''

keyboard = telebot.types.InLineKeyboardMarkup()
keyboard.row(telebot.types.InLineKeyboardButton(' ', callback_data='no'),
             telebot.types.InLineKeyboardButton('C', callback_data='C'),
             telebot.types.InLineKeyboardButton('<=', callback_data='<='),
             telebot.types.InLineKeyboardButton('/', callback_data='/'))
keyboard.row(telebot.types.InLineKeyboardButton('7', callback_data='7'),
             telebot.types.InLineKeyboardButton('8', callback_data='8'),
             telebot.types.InLineKeyboardButton('9', callback_data='9'),
             telebot.types.InLineKeyboardButton('*', callback_data='*'))
keyboard.row(telebot.types.InLineKeyboardButton('4', callback_data='4'),
             telebot.types.InLineKeyboardButton('5', callback_data='5'),
             telebot.types.InLineKeyboardButton('6', callback_data='6'),
             telebot.types.InLineKeyboardButton('-', callback_data='-'))
keyboard.row(telebot.types.InLineKeyboardButton('1', callback_data='1'),
             telebot.types.InLineKeyboardButton('2', callback_data='2'),
             telebot.types.InLineKeyboardButton('3', callback_data='3'),
             telebot.types.InLineKeyboardButton('+', callback_data='+'))
keyboard.row(telebot.types.InLineKeyboardButton(' ', callback_data=' '),
             telebot.types.InLineKeyboardButton('0', callback_data='0'),
             telebot.types.InLineKeyboardButton(',', callback_data=','),
             telebot.types.InLineKeyboardButton('=', callback_data='='))

@bot.massage_handler(commands=['start','go'])
