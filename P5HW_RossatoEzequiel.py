# This program add or substract random numbers
# 5/3/23
# CTI-110 P5HW - Math Quiz
# Ezequiel Rossato
#
import random
def mainFunction():
    randNum1 = random.randint(0, 100)
    randNum2 = random.randint(0, 100)
    print("Welcome to Math Quiz\n")
    matchFunction(randNum1, randNum2)

def matchFunction(randNum1, randNum2): 
    print("\nMAIN MENU")
    print("--------------------")
    print("1. Adding Random Numbers")
    print("2. Substracting Random Numbers")
    print("3. Exit")
    option = int(input("\nPlease choose one of the menu options: "))
    match option:
        case 1:
            calcAddNum(randNum1, randNum2)
            return matchFunction(randNum1, randNum2)
        case 2:
            calcSubNum(randNum1, randNum2)
            return matchFunction(randNum1, randNum2)
        case 3:
            print("Thank ou for playing...\nBye!!")
        case _:
            print("Not valid option, please try again.")
            return matchFunction()
def calcAddNum(randNum1, randNum2):
    print(f' {randNum1}\n+{randNum2}')
    num = randNum1 + randNum2
    guess = 1
    answer = int(input("\nEnter answer: "))
    while answer != num:
        guess += 1
        if answer < num:
            answer = int(input("Sorry, guess is too low.\nTry again: "))
        if answer > num:
            answer = int(input("Sorry, guess is too high.\nTry again: "))
    print(f'Congratulations!!!! Your answer is correct./Number of guesses: {guess}')
def calcSubNum(randNum1, randNum2):
    print(f' {randNum1}\n-{randNum2}')
    num = randNum1 - randNum2
    guess = 1
    answer = int(input("\nEnter answer: "))
    while answer != num:
        guess += 1
        if answer < num:
            answer = int(input("Sorry, guess is too low.\nTry again: "))
        if answer > num:
            answer = int(input("Sorry, guess is too high.\nTry again: "))
    print(f'Congratulations!!!! Your answer is correct./Number of guesses: {guess}')


mainFunction()
