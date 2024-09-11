# Program to bid adieu

import inflect

p = inflect.engine()


def main():

    # List for names
    names = []

    # Ask user for name and adds to list
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break

    # Bid adieu to all
    print(f"Adieu, adieu, to {p.join(names)}")


main()
