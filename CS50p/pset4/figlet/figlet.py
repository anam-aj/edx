# Program to convert text to figlet

import random
import sys
from pyfiglet import Figlet

# Get available fonts
figlet = Figlet()
fonts = figlet.getFonts()


def main():

    if cmnd_line_args_valid():

        # Promts user to enter text
        text = input("Input:  ")

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


def cmnd_line_args_valid():

    # Ensure number of command line arguments is valid
    if not (len(sys.argv) == 1 or len(sys.argv) == 3):
        sys.exit("Please give valid Command Line Argument(s) i.e. '0' or '2'")
    # Check if first argument is valid
    elif sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid arguments")
    # Check if font is valid
    elif sys.argv[2] not in fonts:
        sys.exit("Enter valid font")
    else:
        return True


main()
