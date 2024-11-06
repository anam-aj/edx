# Program to compensate for wrong greeting


def main():

    # Promts user for greeting
    greeting = input("Greeting: ")

    # Prints amount to user
    print(f"${value(greeting)}")


def value(greeting):

    # Strip spaces and converts to lowercase
    greeting = greeting.lower().strip()

    # Check greeting
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
