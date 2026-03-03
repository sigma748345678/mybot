import datetime
import telebot
person = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "hey": "Hey!",
    "bye": "Goodbye!",
    "goodbye": "See you later!",
    "name": "My name is EllyBot",
    "age": "I am 0 years old",
    "python": "Python is awesome!",
    "lua": "Lua is cool too!",
    "help": "Commands: hello, hi, bye, name, age, python, lua, joke, timer, shutdown, youtube = open youtube",
    "joke": "Why did the programmer quit his job? Because he didn't get arrays!",
    "funny": "I love to laugh!",
    "sad": "Don't be sad, cheer up!",
    "happy": "That's great!",
    "thanks": "You're welcome!",
    "thank you": "No problem!",
    "morning": "Good morning!",
    "night": "Good night!",
    "food": "I love pizza!",
    "drink": "Tea is nice",
    "music": "I like chiptune music!",
    "song": "I don't have ears, but I can play tunes!",
    "game": "Do you like games?",
    "play": "I can simulate a dice for you!",
    "dice": "Rolling a dice... 🎲",
    "yes": "Alright!",
    "no": "Okay!",
    "maybe": "Hmm, maybe...",
    "weather": "I don't know the weather, but I hope it's sunny!",
    "date": "Every day is a good day!",
    "love": "Love is in the air!",
    "hate": "I prefer coding to hate.",
    "angry": "Take a deep breath.",
    "fun": "Fun is coding!",
    "bored": "I can tell you a joke!",
    "confused": "Don't worry, I understand!",
    "very stupid": "Everyone learns at their own pace.",
    "smart": "Thanks!",
    "yes please": "As you wish!",
    "no thanks": "No problem!",
    "ok": "Ok!",
    "oops": "It's fine, mistakes happen!",
    "cool": "I'm cool, right?",
    "amazing": "Thanks, I try!",
    "wow": "Wow indeed!",
    "help me": "Just type a command!",
    "shutdown": "Use '-' to shutdown PC",
    "random": "I can do random stuff!",
    "secret": "I know a secret..."
}
telebot = telebot.TeleBot("there not api just use botfaher")
@telebot.message_handler(func=lambda message: True)
def echo_message(message):
    text = message.text.lower().strip()
    if text in person:
        telebot.reply_to(message, person[text])
    elif text == "time":
        now = datetime.datetime.now()
        telebot.send_message(message.chat.id, now.strftime("now: %I:%M:%S %p"))
    else:
        telebot.reply_to(message, "???")
telebot.infinity_polling()