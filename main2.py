#!/usr/bin/env python3
import sys
import random
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"
number = random.randrange(1,1000)
integerBool = False
correctBool = False
while correctBool == False:
    while integerBool == False:
        try:
            guess = input("Guess a number in between 1 and 1000: ")
            guess = int(guess)
            integerBool = True
        except:
            print("Please make sure that you are entering a number.")
    if number == guess:
        print("Wow, that it is very impressive that you were able to guess the number!!")
        correctBool = True
    elif guess > number:
        print("Your guess was higher than the correct number. Please try again.")
        integerBool = False
    else:
        print("Your guess was lower than the correct number. Please try again.")
        integerBool = False

