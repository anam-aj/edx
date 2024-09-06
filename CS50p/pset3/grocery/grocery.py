# Program to place an order


def main():

    while True:

        try:
            item = input("Item: ").title()
            bill += menu[item]
        except KeyError:
            pass
        except EOFError:
            print()
            return
        else:
            print(f"${bill:.2f}")


main()
