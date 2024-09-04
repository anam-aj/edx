# Program to do simple math


def main():

    # Promts user for input
    expression = input("Expression: ")

    # Obtain result
    result = get_result(expression)

    # Print result to user
    print(result)


def get_result(exp):

    # Split input and assign values
    n1, op, n2 = exp.split()

    # Convert string to float
    n1 = float(n1)
    n2 = float(n2)

    # Add
    if op == "+":
        return n1 + n2

    # Subtract
    if op == "-":
        return n1 - n2

    # Product
    if op == "*":
        return n1 * n2

    # Quotient
    if op == "/":
        return n1 / n2


main()
