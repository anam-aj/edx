# Program to convert text to figlet

import sys
from pyfiglet import Figlet


def main():

    # Promts user to enter text
    text = input("Input:  ")

    # Command line argument not given
    if len(sys.argv[]) == 1:
        
    figlet = Figlet()

    print(figlet.renderText(text))


main()
