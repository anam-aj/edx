# Program to convert time from 12-hour format to 24-hour format

import re
import sys


def main():

    # Print time in 24-hour format to user
    print(convert(input("Hours: ")))


def convert(s):

    # Pattern for time
    pattern = "^(?P<start_hour>0?[1-9]|10|11|12):(?P<start_min>0?\d?|[1-5]\d?) AM to (?P<end_hour>[1-9]|10|11|12):(?P<end_min>0\d?|[1-5]\d?) PM$"

    # Find macthing pattern

    # Return time in 24-hour format


if __name__ == "__main__":
    main()
