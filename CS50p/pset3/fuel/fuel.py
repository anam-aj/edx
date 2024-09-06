# Program to convert fraction to percentage


def main():

    # Ask user to enter fraction
    while True:
        fraction = input("Fraction: ")
        numer, denom = fraction.split("/")

        try:
            numer, denom = float(numer), float(denom)
        except ValueError:
            print("Enter numbers not letters")
        except ZeroDivisionError:
            print("Division by zero not allowed")



main()
