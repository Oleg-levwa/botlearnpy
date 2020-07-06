#поиск по шаблону
from glob import glob
import logging
#выбор случайного элемента
from random import choice
#импорт библиотеки астрономии
import ephem
#импорт эмоджи
from emoji import emojize
#модуль разметки клавиатуры
from telegram import ReplyKeyboardMarkup, KeyboardButton

from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler, Filters
import settings

logging.basicConfig (format= '%(asctime)s - %(levelname)s - %(message)s',
                     level=logging.INFO,
                     filename= 'bot.log'
                    )

def greet_user (bot, update, user_data):
    text = 'Вызван /start'
    logging.info (text)
    update.message.reply_text(text, reply_markup = get_keyboard())

#Функция обработки planet
def greet_user_planet (bot, update):
    text = 'Вызван /planet'
    logging.info (text)
    update.message.reply_text(text, reply_markup = get_keyboard())

def talk_to_me (bot, update, user_data):
    user_text = 'Привет, {}! Ты написал: {}'.format(update.message.chat.first_name, update.message.text)
    logging.info ('User: %s, Chat id: %s, Message: %s',
                   update.message.chat.username, update.message.chat.id,
                   update.message.text)
    update.message.reply_text(user_text)
    #Получение названия планеты
    planet = user_text.split(' ')
    planet = planet[4:]
    planet = ' '.join(planet)
    print(planet)
     
def sent_cat_picture (bot, update, user_data):
    cat_list = glob('images/cat*.jp*g')
    cat_pic = choice (cat_list)
    bot.send_photo(chat_id = update.message.chat_id, photo = open(cat_pic, 'rb'), reply_markup = get_keyboard())

def get_contact(bot, update, user_data):
    print(update.message.contact)

def get_location(bot, update, user_data):
    print(update.message.location)

def get_keyboard():
    contact_button = KeyboardButton('Прислать контакты', request_contact = True)
    location_button = KeyboardButton('Прислать координаты', request_location = True)
    my_keyboard = ReplyKeyboardMarkup([
                                        ['Прислать кота', 'Сменить аватарку'],
                                        [contact_button, location_button]
                                       ], resize_keyboard = True)
    return my_keyboard


def main():
    mybot = Updater (settings.API_KEY,
    request_kwargs=settings.PROXY)

    logging.info ('Бот запускается')
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user, pass_user_data = True))
    dp.add_handler(CommandHandler('cat', sent_cat_picture, pass_user_data = True))
    dp.add_handler(RegexHandler('^(Прислать кота)$', sent_cat_picture, pass_user_data = True))
    dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data = True))
    dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data = True))
    #Обработка команды /planet
    dp.add_handler(CommandHandler('planet', greet_user_planet, pass_user_data = True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data = True))

    mybot.start_polling()
    mybot.idle()

main()
