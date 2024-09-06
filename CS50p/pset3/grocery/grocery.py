# Program to place an order


def main():

    # Dictionary to store items
    items = {}

    while True:

        try:
            item = input("Item: ").upper()
            if item in items:
                items[item] += 1
            else:
                items[item] = 1
        except EOFError:
            break

        sortes_items =
        for key in sorted(items):
            print(f"{items[key]} {key}}")
main()
