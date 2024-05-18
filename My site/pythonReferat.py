import telebot
import requests
import json
import math

bot = telebot.TeleBot('7050040517:AAGEvpy_e6GKFborCSccKEYucXUbHr-Tmqc')

API_KEY = '764165b05bba3cebd65a5018e2c6193f'

weather_url = 'http://api.openweathermap.org/data/2.5/weather'

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я бот, который может сообщить тебе текущую погоду. Просто отправь мне название города.')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
    if res.status_code == 200:
        data = json.loads(res.text)
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        round_temp = math.floor(data['main']["temp"])
        temp_humidity = humidity
        bot.reply_to(message, f'Сейчас погода: {round_temp} Градусов, Влажность: {temp_humidity}%, Скорость ветра: {wind_speed} м/с')

        if temp_humidity > 95:
            image = "liven.jpeg"
        elif temp_humidity > 65:
            image = "pasmurna.jpg"
        else:
            image = "sunny.jpeg"

        file = open('./' + image, "rb")
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Город указан неверно')

bot.polling(none_stop=True)


