# Program to tell the number of lines of code

import sys


def main():

    validate_arguments()

    file_name = sys.argv[1]
    with open_file(file_name) as file:

        lines = file.readlines()
        line_count = 0
        # Count the number of (valid)lines
        for line in lines:
            line = line.strip()
            if line and not line.startswith("#"):
                line_count += 1

    # Prints line count to user
    print(line_count)


# Check validity of command line arguments
def validate_arguments():

    # Ensure correct number of comand line argument
    if len(sys.argv) != 2:
        sys.exit("Please give one and only one file name")

    # Ensure name ends with .py
    if not (sys.argv[1]).endswith(".py"):
        sys.exit("Please enter valid python file")


# Ensure file exist
def open_file(file_name):

    try:
        return open(file_name)
    except FileNotFoundError:
        sys.exit("file not found")


if __name__ == "__main__":
    main()
