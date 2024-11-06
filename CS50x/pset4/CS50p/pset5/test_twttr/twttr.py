# Program to omit vowels


def main():

    # Promts user for input
    text = input("Input:  ")

    # Prints the shortened text
    print(shorten(text))


# Remove vowels and return the result
def shorten(word):

    output = ""

    for chr in word:
        if chr.lower() in ["a", "e", "i", "o", "u"]:
            pass
        else:
            output += chr

    return output


if __name__ == "__main__":
    main()
