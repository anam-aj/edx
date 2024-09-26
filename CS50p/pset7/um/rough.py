import re
import sys


def main():

    text = "ab ab cd cd ef ef gh gh"
    pattern = r"(ab)|(cd)|(ef)|(gh)"

    if match := re.findall(pattern, text, re.IGNORECASE):
        print(match)


if __name__ == "__main__":
    main()
