import requests
from bs4 import BeautifulSoup as BS
import random
import telebot

URL = "https://www.anekdot.ru/last/good/"
API_KEY = "6086764618:AAHaYxE9rjEYXx1rOm8EMacwg694DNhETLE"


def parser(url):
    request = requests.get(url)
    soup = BS(request.text, "html.parser")
    anekdots = soup.find_all("div", class_="text")
    return [i.text for i in anekdots]


list_of_anekdots = parser(URL)
random.shuffle(list_of_anekdots)

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=["hello"])
def hello(message):
    bot.send_message(message.chat.id, "Chobi polychit' anekdot preshli lubyu cifru")


@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_anekdots[0])
        del list_of_anekdots[0]
    else:
        bot.send_message(message.chat.id, "Vvedite lubyu cifru")


bot.polling()
