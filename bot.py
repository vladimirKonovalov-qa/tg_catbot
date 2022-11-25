import telebot
import time
import random
 
from telebot import types
 
bot = telebot.TeleBot(token='5944466547:AAHPrdJQYRfAbZnVZOuAmvW27NEiQKK8Gyw', parse_mode='html')

f = open('text.txt', 'r', encoding='UTF-8')
text = f.read().split('\n')
f.close()
 
@bot.message_handler(commands=['start'])
def welcome(message):

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Узнать будущее🔮")
 
    markup.add(item1)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ видела нашу встречу во сне. Присаживайся поудобнее и освободи мысли. Сейчас поведаю, что ждёт тебя впереди".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Привет':
            bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ видела нашу встречу во сне. Присаживайся поудобнее и освободи мысли. Сейчас поведаю, что ждёт тебя впереди".format(message.from_user, bot.get_me()),
        parse_mode='html')
        elif message.text == 'Узнать будущее🔮':
 
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Жмякни🐾", url='https://www.youtube.com/watch?v=5xG09d3WcGo')
 
            markup.add(item1)
 
            time.sleep(1)
            bot.send_message(message.chat.id, 'Магия начинается🧿')
            time.sleep(0.5)
            sti = open('AnimatedSticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
            time.sleep(1)
            bot.send_message(message.chat.id, 'Трах...✨💫⚡')
            time.sleep(1)
            bot.send_message(message.chat.id, 'Тибидох...✨💫⚡🌟')
            time.sleep(1)
            bot.send_message(message.chat.id, 'Тибидох...✨💫⚡🌟💥')
            time.sleep(2)
            bot.send_message(message.chat.id, random.choice(text))
            time.sleep(5)
            bot.send_message(message.chat.id, 'Space chill🚀', reply_markup=markup)
            
        else:
            bot.send_message(message.chat.id, 'Команда /start тебе поможет😉')
 
# RUN
bot.polling(none_stop=True)
