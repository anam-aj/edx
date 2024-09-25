import re
import sys


def main():

    # Prints number of repetetion to user
    print(count(input("Text: ")))


def count(s):

    pattern = r"[^a-zA-Z]+um[^a-zA-Z]+"
    match = re.search(pattern, s, re.IGNORECASE)

    if match := matches.

if __name__ == "__main__":
    main()
