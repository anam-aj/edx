# Program to implement "math professor"

import random


def main():

    # Promt user for level
    level = get_level("Level: ")

    # for



def get_level(string):

    # Promts user for level
    while True:
        level = input(string)

        # Ensure level is valid
        try:
            level = int(level)
            if level not in [1,2,3]:
                raise ValueError
        except:
            pass
        else:
            return level


def generate_integer(level):

    if level == 1:
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(1, 99)
    if level == 3:
        return random.randint(1, 999)


if __name__ == "__main__":
    main()













def main():



    # Set correct value
    correct_value =

    # Ask user for guess
    while True:
        guess = input("Guess: ")

        try:
            # Ensure guess is a positive integer
            guess = int(guess)
            if guess < 1:
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
                return

