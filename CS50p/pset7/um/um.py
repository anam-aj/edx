import re
import sys


def main():

    # Prints number of repetetion to user
    print(count(input("Text: ")))


def count(s):

    pattern = r"\b(um)\b"
    if match := re.findall(pattern, s, re.IGNORECASE):
        count = 0
        print(match)
        #for m in match.groups():
            #if m:
                #count += 1
        #return count
    #else:
        #return 0


if __name__ == "__main__":
    main()
