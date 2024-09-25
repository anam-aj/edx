import re
import sys


def main():

    # Prints number of repetetion to user
    print(count(input("Text: ")))


def count(s):

    pattern = r"(?:^(um)[^a-zA-Z])+|[^a-zA-Z]+(um)[^a-zA-Z]+|(?:[^a-zA-Z]*(um)$)|(?:^(um)$)"
    if match := re.search(pattern, s, re.IGNORECASE):
        print(match.groups())
        return len(match.groups())
    else:
        return 0

if __name__ == "__main__":
    main()
