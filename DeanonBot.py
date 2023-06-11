import requests as r
import telebot
import json
bot = telebot.TeleBot("5920260176:AAFd7cS8gI2bUhIjJC7q7-cSjXJe5dVFzmc")
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Добро пожаловать в Deanon Bot!\n🏘 Поиск по адресу, вводи /address")
@bot.message_handler(commands=['address'])
def address(message):
    address_geolocation = message.text[9:len(message.text)]
    bot.send_message(message.chat.id, f"Пробиваем по адресу {address_geolocation}...")
    try:
        url = r.get(f"https://positionstack.com/geo_api.php?query={address_geolocation}")
        data = json.loads(url.text)
        for key, value in data.items():
            print(f"{key}: {value}")
            bot.send_message(message.chat.id, f"{key}: {value}")
            bot.send_message(message.chat.id, "Там уже сами переобразуете json в текст")
    except:
        bot.send_message(message.chat.id, "Нужно вводить с адресом, а не без адреса /address\nВот например")
        bot.send_message(mesaage.chat.id, "/address Test")
