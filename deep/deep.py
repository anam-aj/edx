# Program to answer the "Great question of life"


def main():

    # Promts user for answer
    answer = input("What is the answer to Great Question of Life? ")

    # Strip spaces and converts to lowercase
    answer = answer.lower().strip()

    # Check answer
    if answer == "42" or answer == "forty two" or answer == "forty-two":
        print("Yes")
    else:
        print("No")


main()
