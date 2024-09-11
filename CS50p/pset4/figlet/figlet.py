# Program to convert text to figlet

import random
import sys
from pyfiglet import Figlet


def main():

    # Check no of command line arguments
    if not (len(sys.argv) == 1 or len(sys.argv) == 3):
        # Check validity of Command line arguments
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid arguments")
        elif sys.argv[2] not in fonts:
            sys.exit("Enter valid font")

        # Promts user to enter text
        text = input("Input:  ")

        figlet = Figlet()
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
            # Prints text in user given font
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(text))

    else:



main()
