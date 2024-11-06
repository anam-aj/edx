# Program to convert text to emoji

import emoji


def main():

    # Promts user to enter text
    text = input("Input:  ")

    # Print emojized text to user
    print(f"Output: {emoji.emojize(text, language='alias')}")


main()
