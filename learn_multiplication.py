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
            print(Fore.BLUE + "your score:", score, "/", "5")
            percent = round((score / 5) * 100, 2)
            print(Fore.GREEN + str(percent) + "%")
        elif cheating == 2:
            time.sleep(2)
            print(Fore.RED + "wait...")
            time.sleep(3)
            print(Fore.RED + "this cheating..")
            time.sleep(6)
            break
print(Fore.CYAN + "math test!")
while True:
    print(Style.RESET_ALL)
    user_choice = input(Fore.LIGHTCYAN_EX + "to start, type 'start' (you can write 'tips' and it will give you the top 5 tips to learn multiplication): ").strip().lower()
    if user_choice == "start":
        mult()
    elif user_choice == "tips":
        print(Fore.RED + math_advice)
