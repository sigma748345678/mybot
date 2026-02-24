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
        g = input("shutdown: yes/no")
        if g == "yes":
            os.system("shutdown /s")
            time.sleep(5)
            break
    elif a == '`': # eto na exit
        print("bye")
        break #break eto tipo konec tipo liv
    else:
        print("???") #bot ne znaet
# ya iz budushego ispravi eto govno pls
