# Program to check validity of IP adresses

import re
import sys


def main():

    # Checks input and Prints result to user
    print(validate(input("IPv4 Address: ")))


# Function to check validity of IPv4 address
def validate(ip):
    pattern = r"^(([01]?\d{0,2}|2[0-4]\d|25[0-5])\.){3}([01]?\d{0,2}|2[0-4]\d|25[0-5])$"

    # Pattern matches
    if re.search(pattern, ip):
        return True
    # Pattern does not match
    else:
        return False


if __name__ == "__main__":
    main()
