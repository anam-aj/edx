import re
import sys


def main():

    text = "ab ab cd cd ef ef gh gh"
    pattern = r"(ab)|(cd)|(ef)|(gh)"
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
