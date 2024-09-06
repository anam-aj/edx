# Program to convert fraction to percentage


def main():

    # Ask user to enter fraction
    while True:
        fraction = get_fraction("Fraction: ")
        if 0 <= fraction <= 1:
            break

    percent = fraction * 100

    if 0 <= percent <= 1:
        print("E")
    elif 99 <= percent <= 100:
        print("F")
    else:
        print(round(percent))

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
