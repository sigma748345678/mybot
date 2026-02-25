import time
import os
person = {"hello": "Hi!", #slovari vsegda v peremenoy
"bye": "Goodbye!",
"name": "My name is EllyBot",
"age": "I am 0 years old",
"python": "Python is awesome! and lua too...",
"help": "Commands: hello, bye, name, age, python, and to exit you need ` , and - this is shutdown pc",
"pizdec ti tupoy": "idi nahuy",
"tupoy": "sam takoy",
"EYY I'M NOT STUPID": "who said",
"suka": "...",
"poka": "pokakayesh doma" #slovar dla bota sam bot nize
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
    elif a == "timer":
        kot = int(input("secunds:"))
        while True:
            time.sleep(1)
            kot -= 1
            print(kot)
            if kot == 0:
                break
    elif a == '`': # eto na exit
        print("bye")
        break #break eto tipo konec tipo liv
    else:
        print("???") #bot ne znaet
# bot made elly5654 (ellychandr5654@gmail.com) (elly5654tt@gmail.com)
