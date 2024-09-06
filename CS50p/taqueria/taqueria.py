# Program to place an order

menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
}


def main():

    bill = 0

    while True:
        item = input("Item: ").lower()
        for key in menu:
        try:
            bill += menu[key]
            print(f"${round(bill, 2)}")

    except EOFError:
        print()
        return

"""
main()


def main():

    bill = 0

    try:
        while True:
            item = input("Item: ").lower()
            for key in menu:
                if item == key.lower():
                    bill += menu[key]
                    print(f"${round(bill, 2)}")

    except EOFError:
        print()
        return


main()
"""
