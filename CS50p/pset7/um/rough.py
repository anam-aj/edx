import re
import sys


def main():

    text = "abc cd ab ef ef gh gh"
    pattern = r"(abc )|(^cd)|(ef)|(gh)"

    if match := re.findall(pattern, text, re.IGNORECASE):
        print(match)


if __name__ == "__main__":
    main()
