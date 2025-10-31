# Program to format pizza menu

import csv
import sys

from tabulate import tabulate


def main():

    validate_arguments()

    file_name = sys.argv[1]

    with open_file(file_name) as file:
        reader = list(csv.reader(file))
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))


# Check validity of command line arguments
def validate_arguments():

    # Ensure correct number of comand line argument
    if len(sys.argv) != 2:
        sys.exit("Please give one and only one file name")

    # Ensure name is a valid CSV file
    if not (sys.argv[1]).endswith(".csv"):
        sys.exit("Please enter valid csv file")


# Ensure file exist
def open_file(file_name):

    try:
        return open(file_name)
    except FileNotFoundError:
        sys.exit("file not found")


if __name__ == "__main__":
    main()
