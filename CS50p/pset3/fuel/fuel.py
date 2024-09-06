# Program to convert fraction to percentage


def main():

    # Ask user to enter fraction
    while True:
        fraction = get_fraction("Fraction: ")
        if 0 <= fraction <= 1:
            break

    # Convert to percent
    percent = fraction * 100

    # Display result
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{round(percent)}%")


def get_fraction(string):

    while True:
        fraction = input(string)

        try:
            numer, denom = fraction.split("/")
            numer, denom = int(numer), int(denom)
            return (numer/denom)
        except ValueError:
            print("Input format 'X/Y' and X,Y are numbers")
        except ZeroDivisionError:
            print("Division by zero not allowed")


main()
