import time
from colorama import Fore, Style
from random import randint
math_advice = """
1. Learn the multiplication table – Knowing times tables by heart makes calculations much faster.
2. Use the distributive property – Break numbers into easier parts (e.g., 12 × 4 = (10 × 4) + (2 × 4)).
3. Multiply in parts – Split large numbers into smaller ones to simplify the problem.
4. Use patterns – Notice patterns like multiplying by 10, 100, or 5 to make quick mental math easier.
5. Practice regularly – The more you practice, the faster and more accurate you become
"""
def mult():
    score = 0
    trys = 0
    cheating = 0
    while trys < 5:
        print(Style.RESET_ALL)
        random_multiplication1 = randint(1, 10)
        random_multiplication2 = randint(1, 10)
        true_answer = random_multiplication1 * random_multiplication2
        time.sleep(1)
        print("what is", random_multiplication1, "*", random_multiplication2)
        try:
            user_input = int(input("answer: "))
            if user_input == true_answer:
                print(Fore.GREEN + "True!!!")
                trys += 1
                score += 1
            else:
                print(Fore.RED + "False!")
                trys += 1
                print(Fore.LIGHTBLUE_EX + "True answer:", true_answer)
        except ValueError:
            print(Fore.LIGHTRED_EX + "you can only enter numbers there.")
            cheating += 1
        if trys == 5:
            print(Fore.BLUE + "your score:", score, "/", trys)
            percent = round((score / 5) * 100, 2)
            print(Fore.GREEN + str(percent) + "%")
        elif cheating == 2:
            time.sleep(2)
            print(Fore.BLUE + "your score:", score, "/", trys)
            percent_cheat = round((score / 5) * 100, 2)
            print(Fore.GREEN + str(percent_cheat) + "%")
            break # this break just return in the main menu

def addi():
    score = 0
    trys = 0
    cheating = 0
    while trys < 5:
        print(Style.RESET_ALL)
        random_addion1 = randint(1, 10)
        random_addion2 = randint(1, 10)
        true_answer = random_addion1 + random_addion2
        time.sleep(1)
        print("what is", random_addion1, "+", random_addion2)
        try:
            user_input = int(input("answer: "))
            if user_input == true_answer:
                print(Fore.GREEN + "True!!!")
                trys += 1
                score += 1
            else:
                print(Fore.RED + "False!")
                trys += 1
                print(Fore.LIGHTBLUE_EX + "True answer:", true_answer)
        except ValueError:
            print(Fore.LIGHTRED_EX + "you can only enter numbers there.")
            cheating += 1
        if trys == 5:
            print(Fore.BLUE + "your score:", score, "/", trys)
            percent = round((score / 5) * 100, 2)
            print(Fore.GREEN + str(percent) + "%")
        elif cheating == 2:
            time.sleep(2)
            print(Fore.BLUE + "your score:", score, "/", trys)
            percent_cheat = round((score / 5) * 100, 2)
            print(Fore.GREEN + str(percent_cheat) + "%")
            break # this break just return in the main menu

def sub():
    score = 0
    trys = 0
    cheating = 0
    while trys < 5:
        print(Style.RESET_ALL)
        random_sub1 = randint(1, 10)
        random_sub2 = randint(1, 10)
        if random_sub1 < random_sub2:
            random_sub1, random_sub2 = random_sub2, random_sub1
        true_answer = random_sub1 - random_sub2
        time.sleep(1)
        print("what is", random_sub1, "-", random_sub2)
        try:
            user_input = int(input("answer: "))
            if user_input == true_answer:
                print(Fore.GREEN + "True!!!")
                trys += 1
                score += 1
            else:
                print(Fore.RED + "False!")
                trys += 1
                print(Fore.LIGHTBLUE_EX + "True answer:", true_answer)
        except ValueError:
            print(Fore.LIGHTRED_EX + "you can only enter numbers there.")
            cheating += 1
        if trys == 5:
            print(Fore.BLUE + "your score:", score, "/", trys)
            percent = round((score / 5) * 100, 2)
            print(Fore.GREEN + str(percent) + "%")
        elif cheating == 2:
            time.sleep(2)
            print(Fore.BLUE + "your score:", score, "/", trys)
            percent_cheat = round((score / 5) * 100, 2)
            print(Fore.GREEN + str(percent_cheat) + "%")
            break # this break just return in the main menu

def div():
    score = 0
    trys = 0
    cheating = 0
    while trys < 5:
        print(Style.RESET_ALL)
        random_div1 = randint(1, 10)
        random_div2 = randint(1, 10)
        if random_div1 < random_div2:
            random_div1, random_div2 = random_div2, random_div1
        true_answer = round(random_div1 / random_div2)
        time.sleep(1)
        print("what is", random_div1, "/", random_div2)
        try:
            user_input = int(input("answer: "))
            if user_input == true_answer:
                print(Fore.GREEN + "True!!!")
                trys += 1
                score += 1
            else:
                print(Fore.RED + "False!")
                trys += 1
                print(Fore.LIGHTBLUE_EX + "True answer:", true_answer)
        except ValueError:
            print(Fore.LIGHTRED_EX + "you can only enter numbers there.")
            cheating += 1
        if trys == 5:
            print(Fore.BLUE + "your score:", score, "/", trys)
            percent = round((score / 5) * 100, 2)
            print(Fore.GREEN + str(percent) + "%")
        elif cheating == 2:
            time.sleep(2)
            print(Fore.BLUE + "your score:", score, "/", trys)
            percent_cheat = round((score / 5) * 100, 2)
            print(Fore.GREEN + str(percent_cheat) + "%")
            break # this break just return in the main menu

print(Fore.CYAN + "math test!")
while True:
    print(Style.RESET_ALL)
    user_choice = input(Fore.LIGHTCYAN_EX + "to start, type 'multiplication/addion/subtraction/division' (you can write 'tips' and it will give you the top 5 tips to learn multiplication): ").strip().lower()
    if user_choice == "multiplication":
        mult()
    elif user_choice == "addion":
        addi()
    elif user_choice == "subtraction":
        sub()
    elif user_choice == "division":
        div()
    elif user_choice == "tips":
        print(Fore.RED + math_advice)
# made ellychandr5654@gmail.com