# Program to place an order


def main():

    while True:

        try:
            item = input("Item: ").title()
        except EOFError:
            print()
            return


main()
