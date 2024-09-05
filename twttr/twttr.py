# Program to omit vowels


def main():

    # Promts user for input
    inpt = input("Input:  ")

    # Remove vowels and print the result
    for chr in inpt:
        if chr.lower() in ["a", "e", "i", "o", "u"]:
            print("", end="")
        else:
            print(chr, end="")

    print()


main()
