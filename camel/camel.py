# Program to convert camelCase to snake_case


def main():

    # Promts user for input
    camel_case = input("camelCase:  ")

    # Coverts into snake_case
    snake_case = make_snake_case(camel_case)

    # Print snake_case to user
    print(f"snake_case: {snake_case}")


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
