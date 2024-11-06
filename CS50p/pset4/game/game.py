# program to implement guessing game

import random


def main():

    # Promts user for level
    while True:
        level = input("Level: ")

        # Ensure level is a positive integer
        try:
            level = int(level)
            if level < 1:
                raise ValueError
        except:
            pass
        else:
            break

    # Set correct value
    correct_value = random.randint(1, level)

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


if __name__ == "__main__":
    main()
