# Program to convert fraction to percentage


def main():

    # Ask user to enter fraction


def get_fraction(string):

    while True:
        fraction = input(string)
        numer, denom = fraction.split("/")

        try:
            numer, denom = float(numer), float(denom)
            break
        except ValueError:
            print("Input format 'X/Y' and X,Y are numbers")
        except ZeroDivisionError:
            print("Division by zero not allowed")


main()
