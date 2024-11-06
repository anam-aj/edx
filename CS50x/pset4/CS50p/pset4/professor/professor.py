# Program to implement "math professor"

import random


def main():

    # Promt user for level
    level = get_level()
    print(f"Level: {level}")

    # Variable to track score
    score = 0

    # Ask 10 questions to user
    for _ in range(10):

        # Generate 2 random integers
        x = generate_integer(level)
        y = generate_integer(level)

        # Varible to track if unser answers correctly
        correct_ans = False

        # Give 3 tries to answer the question correctly
        for _ in range(3):
            # Ask question
            user_ans = input(f"{x} + {y} = ")
            # Check answer
            try:
                user_ans = int(user_ans)
                if user_ans != x + y:
                    raise ValueError
            except:
                print("EEE")
            else:
                # When user answers correctly
                score += 1
                correct_ans = True
                break

        if not correct_ans:
            print(f"{x} + {y} = {x + y}")

    # Print Final Score
    print(f"Score: {score}")


def get_level():

    # Promts user for level
    while True:
        level = input("Level: ")

        # Ensure level is valid
        try:
            level = int(level)
            if level not in [1, 2, 3]:
                raise ValueError
        except:
            pass
        else:
            return level


def generate_integer(level):

    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
