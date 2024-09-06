# Program to place an order


def main():

    # Dictionary to store items
    items = {}

    # Promts user for iteam and add them to dictionary
    while True:
        try:
            item = input().upper()
            if not item:
                pass
            elif item in items:
                items[item] += 1
            else:
                items[item] = 1
        except EOFError:
            print()
            break

    # Print items (sorted alphabetically)
    for key in sorted(items):
        print(f"{items[key]} {key}")


main()
