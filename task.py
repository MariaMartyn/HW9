import telebot
from math import *
import random

bot = telebot.TeleBot("5907898080:AAE81OzG4Q7-oWUVXHGIt1J034BFdd94GSU", parse_mode=None)


@bot.message_handler(content_types=["text"])
def welcome(message):
    global number
    global count
    global decide
    global flag
    findNumber = 0

    if 'привет' in message.text:
        flag = False
        decide = False
        bot.reply_to(message, 'привет, ' + message.from_user.first_name)

    elif message.text == 'давай играть':
        flag = True
        decide = False
        count = 0
        number = random.randint(1, 1000)
        bot.reply_to(message, f'Давай, я загадал число от 1 до 1000.\nПопробуй отгадай: ')

    elif message.text == 'реши уравнение':
        decide = True
        flag = False
        bot.reply_to(message, f'Давай, я готов')

    if decide==True:
        func = str(message.text)
        try:
            bot.send_message(message.from_user.id, eval(func))
        finally:
            decide == False
        
    if flag==True:
        if message.text.isdigit():
            findNumber = int(message.text)
            if findNumber > number:
                bot.send_message(message.from_user.id, f'Нет, мое число меньше. Попробуй еще раз')
            elif findNumber < number:
                bot.send_message(message.from_user.id, f'Нет, мое число больше. Попробуй еще раз')
            else:
                  bot.send_message(message.from_user.id, f'Угадал! Это число {number}, ты угадал за {count} ходов')
        else:
            if count!=0:
                bot.send_message(message.from_user.id, f'Это не число. Введи число')
        count +=1
    else:
        flag = False

bot.infinity_polling()