'''
* Author: Tyler Knight
* Date: 1//28/2019
* Purpose: A number Guessing Game
'''

import random
import os
import functions as func

__name__ = "__main__"


def main():
  
    #Variables: --> user_guess, user_input, attempts_remaining, random_number, guess_range

    while True:
        #Generate random_number, attempts and the guess range
        random_number = func.generate_random()
        attempts_remaining = func.generate_attempts(random_number)
        guess_range = func.get_range(random_number)

        #While the user still has attempts left do..
        while attempts_remaining > 0:

            #Catches user input error
            while True:
                try:
                    print("Attempts remaining: {0}".format(attempts_remaining))
                    user_guess = int(input("Enter a number between 1 and {0}\n".format(guess_range)))
                    break
                except:
                    print("That wasn't a number, try again")

            #Checks to see if they guessed correctly
            if func.check_guess(random_number, user_guess, guess_range):
                break
            else:
                attempts_remaining = attempts_remaining - 1

        #Checks win/loss status
        func.win_loss_status(random_number, attempts_remaining)

        #Initialize user_input
        user_input = str();

        while (user_input != "yes") or (user_input != "no"):
            user_input = str(input("Play again? yes/no\n"))

            if user_input.lower() == "no":
                os._exit(0)
            else:
                break

"""Main Function"""
if __name__ == "__main__":
    main()



