# Program to convert camelCase to snake_case


def main():

    # Promts user for input
    camel_case = input("camelCase: ")

    # Coverts into snake_case
    snake_case = make_snake_case(camel_case)

    # Print snake_case to user
    print(snake_case)


# Convert 
def make_snake_case(string):

    for chr in string:
        if chr.isupper():
            print(f"_{chr.lower()}", end="")
        else:
            print(chr, end="")

    print()


main()
