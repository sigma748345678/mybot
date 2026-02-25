import time
import os
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
    "help": "Commands: hello, hi, bye, name, age, python, lua, joke, timer, shutdown",
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
    "stupid": "Everyone learns at their own pace.",
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
while True:  #beskonechni cikl
    a = input("you:").lower().strip() #lover dla togo chtobi koda bila tak: HELLO to ono otvechalo a string che bi kogda bili probeli toze otvechal
    if a in person: #chem gushe les if else if else
        print("bot:", person[a]) #vivod
    elif a == "-":
        g = input("shutdown: yes/no").lower().strip()
        if g == "yes":
            os.system("shutdown /s") #virubanie pc
            time.sleep(5)
            break
    elif a == "time":
        concurrent_time = time.strftime("%H:%M:%S")
        print(concurrent_time)
        lol = input("for what you use this, you dont have clock on pc?").lower().strip()
        if lol == "yes":
            print("okeeeeeyyyy")
        else:
            print(".....")
            break
    elif a == "timer":
        kot = int(input("secunds:"))
        while True:
            time.sleep(1)
            kot -= 1
            print(kot)
            if kot == 0:
                print('this end')
                break
    elif a == '`': # eto na exit
        print("bye")
        break #break eto tipo konec tipo liv
    else:
        print("???") #bot ne znaet
# bot made elly5654 (ellychandr5654@gmail.com) (elly5654tt@gmail.com)
