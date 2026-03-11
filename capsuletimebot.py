import telebot
import time
import datetime
import os
user_words = {}
bot = telebot.TeleBot("there not api")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    date = datetime.datetime.now()
    bot.send_message(message.chat.id, date)
    bot.send_message(message.chat.id, "hi this is a time capsule bot")
    time.sleep(0.2)
    bot.send_message(message.chat.id, "write what you want to write to yourself so that you can get it in 5 years")
    text = message.text
    user_words[len(user_words)] = text
    time.sleep(157680000)
    bot.send_message(message.chat.id, text)
bot.polling()
