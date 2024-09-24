import re
import sys


def main():

    # Prints the shortend video-link
    print(parse(input("HTML: ")))


def parse(s):

    # Search for youtube link
    pattern = r'iframe src="https?://(?:www.)?youtube.com/embed/(.+)"></iframe>'

    # Shortens the link and return it
    if match := re.search(pattern, s):
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    else:
        return None


if __name__ == "__main__":
    main()
