# Program to place an order


def main():

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


# Convert camelCase to snake_case
def make_snake_case(string):

    snake_case = ""

    for chr in string:
        if chr.isupper():
            snake_case += "_" + chr.lower()
        else:
            snake_case += chr

    return snake_case


main()
