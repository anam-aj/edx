# program to implement guessing game

import random


def main():

    # Promts user for level
    while True:
        level = input("Level: ")

        try:
            level = int(level)
            if level < 1:
                # print("Level has to be a positive integer")
                raise ValueError
        except:
            pass
        else:
            break

    correct_value = random.randint(1, level)

    # Ask user for guess
    while True:
        guess = input("Guess: ")

        try:
            guess = int(guess)
            if guess < 1:
                # print("Level has to be a positive integer")
                raise ValueError
        except:
            pass
        else:
            # Check if user's guess is correct
            if guess < correct_value:
                print("Too small!")
            elif guess > correct_value:
                print("Too large!")
            else:
                print("Just right!")
                return 0


main()
