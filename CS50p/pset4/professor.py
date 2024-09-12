# program to implement "math professor"

import random



import random


def main():



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
    ...


if __name__ == "__main__":
    main()













def main():



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
