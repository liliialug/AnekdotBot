import requests
import random
import telebot
from bs4 import BeautifulSoup as b
API_KEY = '5579050143:AAGzd-Zyd4G0sfaGOgPxv0HetQvo8CgyMUY'
URL = 'https://www.anekdot.ru/last/good/'
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['start'])

def hello(message):
    bot.send_message(message.chat.id, 'Привет! Чтобы порофлить введи любую цифру:')

@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '1234567890':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Введи любую цифру:')

bot.polling()
