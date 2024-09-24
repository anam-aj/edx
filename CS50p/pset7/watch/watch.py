import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'iframe src="https?://(?:www.)?youtube.com/embed/(.+)"></iframe>'

    if match := re.search(pattern, s):
        match.group(1)


if __name__ == "__main__":
    main()
