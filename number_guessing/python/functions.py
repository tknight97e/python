"""
* Author: Tyler Knight
* Date: 1/28/2019
* Purpose: Stores the functions for main.py
"""


import random

def generate_random():
    """Generates a number 1-100"""
    return random.randint(1, 101)


def generate_attempts(random_number):
    """Generates user attempts based on random_number value"""
    if random_number <= 10:
        return 2
    elif random_number <= 25:
        return 4
    elif random_number <= 50:
        return 5
    elif random_number <= 75:
        return 7
    else:
        return 10

def get_range(random_number):
    """Determines the guess range based on random_number value"""
    if random_number <= 10:
        return 10
    elif random_number <= 25:
        return 25
    elif random_number <= 50:
        return 50
    elif random_number <= 75:
        return 70
    else:
        return 100

def check_guess(random_number, user_guess, guess_range):
    """Checks the user_guess to see if it's right, or even in the number range"""
    if user_guess == random_number:
        return True
    else:
        if (user_guess < 1) or (user_guess > guess_range):
            print("Thats not even in the number range!!")
            return False
        elif user_guess < random_number:
            print("Too Low!")
            return False
        elif user_guess > random_number:
            print("Too High!")
            return False
        else:
            print("Not sure what you did there.")
            return False


def win_loss_status(random_number, attempts_remaining):
    """Checks to see if the user won/lost"""
    if attempts_remaining > 0:
        print("You Won!")
        print("The random number was {0}".format(random_number))
    else:
        print("You Lost!")
        print("The random number was {0}".format(random_number))