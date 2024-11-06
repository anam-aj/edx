import re
import sys


def main():

    # Prints number of repetetion to user
    print(count(input("Text: ")))


def count(s):

    # regex to find all "ums"
    pattern = r"\b(um)\b"

    # Find number of "um" case insensitively and return it
    if match := re.findall(pattern, s, re.IGNORECASE):
        return len(match)
    else:
        return 0


if __name__ == "__main__":
    main()
