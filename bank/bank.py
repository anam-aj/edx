# Program to compensate for wrong greeting


def main():

    # Promts user for greeting
    greeting = input("Greeting: ")

    # Strip spaces and converts to lowercase
    greeting = greeting.lower().strip()

    # Check greeting
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")


main()
