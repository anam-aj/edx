# Program to compensate for wrong greeting


def main():

    # Promts user for greeting
    greeting = input("Greeting: ")

    # Split greeting into words
    words = greeting.split()

    # Check greeting
    first_word = words[0].lower()

    if first_word == "hello":
        print("$0")


main()
