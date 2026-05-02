import webbrowser
import time
import os
from colorama import Fore, Style
import pyautogui
while True:
    time.sleep(1)
    print(Fore.LIGHTCYAN_EX + "HELLO I'M HELPER BOT!")
    print('what i can do: shut down pc, open youtube, open gmail')
    print('comands: open youtube')
    print('shut down pc')
    print('open gmail')
    print("open gmail with write")
    print('(down pc) (youtube) (gmail)')
    print(Style.RESET_ALL)
    user = input(Fore.YELLOW + "you: ").strip().lower()
    if user == "shut down pc" or user == "down pc":
        os.system("shutdown /s")
    elif user == "open youtube" or user == "youtube":
        webbrowser.open("youtube.com")
    elif user == "open gmail" or user == "gmail":
        webbrowser.open("gmail.com")
    elif user == "open gmail with write":
        webbrowser.open("gmail.com")
        time.sleep(3)
        pyautogui.moveTo(186, 219)
        pyautogui.click()
        pyautogui.moveTo(1427, 526)
        pyautogui.click()
        pyautogui.moveTo(1380, 609)
        pyautogui.click()
        pyautogui.write('THANKS FOR USING HELPER BOT!')
        pyautogui.press('enter')
        pyautogui.write('#made ellychandr5654@gmail.com')