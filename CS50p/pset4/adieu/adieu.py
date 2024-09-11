# Program to bid adieu

import inflect

p = inflect.engine()


def main():

    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break

    print(p.join(names))


main()
