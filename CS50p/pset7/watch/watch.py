import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'iframe src="https?://(?:www.)?youtube.com/embed/(.+)"></iframe>'


if __name__ == "__main__":
    main()
