#!/usr/bin/env python3
# Created by: Jonathan Kene
# Created on: May 11 2021
# This program asks the user to guess a number between 0 to 9
# and tells the user if the guess is right or wrong

import random


def main():

    # generate a number between 0 to 9
    correct_guess = random.randint(0, 9)

    # get the user's guess
    user_guess = int(input("Enter the number between 0 and 9: "))
    print("")

    # check to see if the user guess is correct or wrong
    if user_guess == correct_guess:
        print("You are correct!")
    else:
        print("You are wrong! The answer is = ")
        print(correct_guess)


if __name__ == "__main__":
    main()
