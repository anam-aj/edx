# Program to convert text to figlet

import sys
from pyfiglet import Figlet


def main():

    # Promts user to enter text
    text = input("Input:  ")

    # Command line argument not given
    if len(sys.argv[]) == 1:
        # Prints text in random font
        
    elif len(sys.argv[]) == 3:
        # Prints text in user given font
    else:
        sys.exit("Please give valid Command Line Argument(s) i.e. '0' or '2'")


    figlet = Figlet()

    print(figlet.renderText(text))


main()
