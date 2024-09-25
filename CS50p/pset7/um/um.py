import re
import sys


def main():

    # Prints number of repetetion to user
    print(count(input("Text: ")))


def count(s):

    pattern = r"(?:^(um)[^a-zA-Z])+|[^a-zA-Z]+(um)[^a-zA-Z]+|(?:[^a-zA-Z]*(um)$)|(?:^(um)$)"
    match = re.search(pattern, s, re.IGNORECASE)
    count = 0
    for m in match.groups():
        if m:
            count += 1

    return count

if __name__ == "__main__":
    main()
