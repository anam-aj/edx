# Program to convert text to figlet

import random
import sys
from pyfiglet import Figlet


def main():


    figlet = Figlet()
    # Get available fonts
    fonts = figlet.getFonts()
    print(fonts)


main()
