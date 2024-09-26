import re
import sys


def main():

    # Prints number of repetetion to user
    print(count(input("Text: ")))


def count(s):

    pattern = r"\b(um)\b"
    if match := re.findall(pattern, s, re.IGNORECASE):
        return len(match)
    else:
        return 0


if __name__ == "__main__":
    main()
