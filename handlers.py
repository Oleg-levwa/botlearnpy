#поиск по шаблону
from glob import glob
#выбор случайного элемента
from random import choice
from utils import get_keyboard
import logging
def greet_user (bot, update, user_data):
    text = 'Вызван /start'
    logging.info (text)
    update.message.reply_text(text, reply_markup = get_keyboard())

def talk_to_me (bot, update, user_data):
    user_text = 'Привет, {}! Ты написал: {}'.format(update.message.chat.first_name, update.message.text)
    logging.info ('User: %s, Chat id: %s, Message: %s',
                   update.message.chat.username, update.message.chat.id,
                   update.message.text)
    update.message.reply_text(user_text)
    
     
def sent_cat_picture (bot, update, user_data):
    cat_list = glob('images/cat*.jp*g')
    cat_pic = choice (cat_list)
    bot.send_photo(chat_id = update.message.chat_id, photo = open(cat_pic, 'rb'), reply_markup = get_keyboard())

def get_contact(bot, update, user_data):
    print(update.message.contact)

def get_location(bot, update, user_data):
    print(update.message.location)