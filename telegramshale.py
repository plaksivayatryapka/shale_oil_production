#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import telepot
#from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from functions import draw_model

token = '233453069:AAH3dL4PJK8CJxdMshGTUuZNdsm2RS8oP4I' # id бота
TelegramBot = telepot.Bot(token)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg) # получаем параметры сообщения
    input_data = msg['text'] # текст сообщения присваиваем переменной input_data
    print 'data :', content_type, chat_type, input_data # печать в консоль справочной информации

    # клавиатура на экране телеграм
    
    #keyboard = InlineKeyboardMarkup(inline_keyboard = [[InlineKeyboardButton (text='Press me', callback_data='yes')], [InlineKeyboardButton (text='Press me2', callback_data='no') ], ])
    #TelegramBot.sendMessage(chat_id, 'Use')
    #TelegramBot.sendMessage(chat_id, 'Use inline keyboard', reply_markup=keyboard)
    
    if input_data == '/start' : # если это начало разговора с ботом, то вывести:
        TelegramBot.sendMessage(chat_id, u'Введите данные для модели добычи "сланцевой" нефти. Например: 12 0.6 1 \
\nГде первое число это срок прогноза в месяцах, а остальное это сценарии количества буровых \
в виде доли от исторического максимума. В данном примере это 60% и 100%')
    else:
        input_data = input_data.split() # введённый текст переделываем в массив
        input_data = list(map(float, input_data)) # сценарии буровых в float
        input_data[0] = int(input_data[0]) # месяцы в int
        draw_model(input_data) # запуск модели с входными параметрами
        time.sleep(1) 
        TelegramBot.sendPhoto(chat_id, open('chart.png', 'rb')) # отправка графика в чат
    

TelegramBot.message_loop(handle) # постоянно крутящаяся функция приёма сообщений
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
