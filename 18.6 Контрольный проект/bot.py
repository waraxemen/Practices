import telebot
import requests
import json
from extensions import APIException
from config import TOKEN
bot = telebot.TeleBot(TOKEN)

keys = {"евро": "EUR", "доллар": "USD", "рубль": "RUB"}

@bot.message_handler(commands=['start','help'])
def help(message: telebot.types.Message):
    text = "Чтобы рассчитать курс валюты - введите название валюты с маленькой буквы, доступны:  евро, доллар, рубль.\
\n Через пробел введите в какую валюту хотите перевести, \nпробел и количество валюты цифрами для перевода "
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values (message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = '\n'.join((text,key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIException('Должно быть 3 параметра.\n')
        quote, base, amount = values
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        total_base = json.loads(r.content)[keys[base]] * abs(float(amount))
        if quote == base:
            text = f'Смысла в этом особого нет, но давайте посчитаем =) :'
            bot.send_message(message.chat.id, text)
    except ValueError as e: bot.reply_to(message, f'Количество нужно вводить цифрами. Попробуйте ещё раз')
    except Exception as e: bot.reply_to(message, f'Ошибка ввода: \n{e}')
    else:
        text = f'Цена {amount} {quote} - {total_base} {base} '
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)