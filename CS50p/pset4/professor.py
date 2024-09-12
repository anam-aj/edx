# Program to implement "math professor"

import random


def main():

    # Promt user for level
    level = get_level("Level: ")
    print(f"Level: {level}")

    # Ask questions to user
    for q in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        user_ans = input(f"{x} + {y} = ")

        try:
            user_ans = int(user_ans)
            if user_ans != x + y:
                raise ValueError
        except:
            print("EEE")
        else:




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
