import re
import sys


def main():

    text = "abc cd cd ef ef gh gh"
    pattern = r"(ab)|(abc)|(ef)|(gh)"

    if match := re.findall(pattern, text, re.IGNORECASE):
        print(match)


if __name__ == "__main__":
    main()
