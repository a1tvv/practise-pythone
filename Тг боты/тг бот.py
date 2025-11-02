import telebot
import requests
import json

bot = telebot.TeleBot("7022258546:AAG_bcOHkxwmZq-Og6ygY7hdu9vL7aFocCU")
API = "0d428c718eae46acc97cd511403347c1"


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data['main']['temp']
        bot.reply_to(message, f'Сейчас погода:  {temp}')

        image = 'sun.png' if temp > 5.0 else 'sunny.png'
        with open(image, 'rb') as file:
            bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message,f'Город указан не верно')

bot.polling(none_stop=True)