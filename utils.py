#выбор случайного элемента
from random import choice
#импорт эмоджи
from emoji import emojize
#модуль разметки клавиатуры
from telegram import ReplyKeyboardMarkup, KeyboardButton

import settings

def get_keyboard():
    contact_button = KeyboardButton('Прислать контакты', request_contact = True)
    location_button = KeyboardButton('Прислать координаты', request_location = True)
    my_keyboard = ReplyKeyboardMarkup([
                                        ['Прислать кота', 'Сменить аватарку'],
                                        [contact_button, location_button]
                                       ], resize_keyboard = True)
    return my_keyboard