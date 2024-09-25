import re
import sys


def main():

    # Prints number of repetetion to user
    print(count(input("Text: ")))


def count(s):

    pattern = r"[^a-zA-Z]*(um)[^a-zA-Z]*"
    if match := re.search(pattern, s, re.IGNORECASE):
        return len(match)
    else:
        return 0

if __name__ == "__main__":
    main()
