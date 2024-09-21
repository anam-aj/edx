# Program to tell the number of lines of code

import sys


def main():

    # Ensure correct number of comand line argument
    if len(sys.argv) != 2:
        sys.exit("Please give one and only one file name")

    # Ensure name ends with .py
    if not (sys.argv[1]).endswith(".py"):
        sys.exit("Please enter valid python file")

    # Ensure file exist
    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("file not found")

    # Count the no of (valid)lines
    lines = file.readlines()
    line_count = 0

    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            line_count += 1

    file.close()

    # Prints line count to user
    print(line_count)


main()
