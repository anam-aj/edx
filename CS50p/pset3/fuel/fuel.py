# Program to convert fraction to percentage


def main():

    # Ask user to enter fraction
    fraction = get_fraction("Fraction: ")






def get_fraction(string):

    while True:

        fraction = input(string)

        try:
            numer, denom = fraction.split("/")
            numer, denom = float(numer), float(denom)
            return (numer/denom)
        except ValueError:
            print("Input format 'X/Y' and X,Y are numbers")
        except ZeroDivisionError:
            print("Division by zero not allowed")


main()
