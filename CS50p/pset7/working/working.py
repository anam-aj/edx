# Program to convert time from 12-hour format to 24-hour format

import re
import sys


def main():

    # Print time in 24-hour format to user
    print(convert(input("Hours: ")))


def convert(s):

    # Pattern for time
    pattern1 = r"^(?P<start_hour>0?[1-9]|10|11|12):(?P<start_min>0?\d|[1-5]\d) AM to (?P<end_hour>0?[1-9]|10|11|12):(?P<end_min>0?\d|[1-5]\d) PM$"

    # Find macthing pattern
    if match := re.search(pattern1, s.strip()):
        start_hr = match.group("start_hour")
        start_mn = match.group("start_min")
        end_hr = match.group("end_hour")
        end_mn = match.group("end_min")

    # Return time in 24-hour format


if __name__ == "__main__":
    main()
