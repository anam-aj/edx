# Program to convert text to figlet

import random
import sys
from pyfiglet import Figlet


def main():

    # Promts user to enter text
    text = input("Input:  ")

    # Get available fonts
    fonts = figlet.getFonts()

    # Command line argument not given
    if len(sys.argv) == 1:
        # Get random font
        rand_font = random.choice(fonts)
        figlet.setFont(font=rand_font)
        # Prints text in random font
        print(figlet.renderText(text))

    # Command line arguments given
    elif len(sys.argv) == 3:
        # Check Command line arguments
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid arguments")
        elif sys.argv[2] not in fonts:
            sys.exit("Enter valid font")
        else:

        # Get user font

        figlet.setFont(font=rand_font)
        # Prints text in user given font

    else:
        sys.exit("Please give valid Command Line Argument(s) i.e. '0' or '2'")


    figlet = Figlet()

    print(figlet.renderText(text))


main()
