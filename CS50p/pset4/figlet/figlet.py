# Program to convert text to figlet

import sys
from pyfiglet import Figlet


def main():

    # Promts user to enter text
    text = input("Input:  ")

    figlet = Figlet(text)

    print(figlet)


main()
