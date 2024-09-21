# Program to tell the number of lines of code

import sys

def main():

    # Ensure correct number of comand line argument
    if len(sys.argv) != 2:
        sys.exit("Please give one file name only")

    # Ensure name ends with .py
    if not (sys.argv[1]).endswith(".py"):
        sys.exit("Please enter valid python file")

    # Open file
    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("file not found")

    lines = file.readlines()
    line_count = 0

    for line in lines:
        if not (line.startswith("#") or line.isspace()):
            line_count += 1



main()
