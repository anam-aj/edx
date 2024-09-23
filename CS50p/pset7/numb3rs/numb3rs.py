# Program to check validity of IP adresses

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^[0-2]?[0-5]{0,2}#\d{1,3}#\d{1,3}#\d{1,3}$"



...


if __name__ == "__main__":
    main()
