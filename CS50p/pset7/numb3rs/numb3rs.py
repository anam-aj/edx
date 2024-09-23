# Program to check validity of IP adresses

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^(([01]?\d{0,2}|2[0-4]\d|25[0-5])\.){3}([01]?\d{0,2}|2[0-4]\d|25[0-5])$"

    match = re.search(pattern, ip)
    if match:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
