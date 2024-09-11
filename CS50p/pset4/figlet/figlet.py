# Program to convert text to figlet

import random
import sys
from pyfiglet import Figlet


def main():

    # Promts user to enter text
    text = input("Input:  ")

    # Command line argument not given
    if len(sys.argv) == 1:
        # Get random font
        fonts = figlet.getFonts()
        rand_font = random.choice(fonts)
        figlet.setFont(font=rand_font)
        # Prints text in random font
        print(figlet.renderText(text))

    elif len(sys.argv) == 3:
        # Check Command line arguments
        
        # Get user font

        figlet.setFont(font=rand_font)
        # Prints text in user given font

    else:
        sys.exit("Please give valid Command Line Argument(s) i.e. '0' or '2'")


    figlet = Figlet()

    print(figlet.renderText(text))


main()
