# Program to convert fraction to percentage


def main():

    # Ask user to enter fraction
    while True:
        fraction = input("Fraction: ")
        if convert(fraction):
            fraction = convert(fraction)
            break

    # Convert to percent
    percent = int(round(fraction * 100))

    # Print result to user
    print(gauge(percent))


def convert(fraction):

    try:
        numer, denom = fraction.split("/")
        # Ensure both numerator and denominator are integers
        if not numer.isdigit() or not denom.isdigit():
            raise ValueError
        # Ensure fraction is not greater than 1
        numer, denom = int(numer), int(denom)
        if numer > denom:
            raise ValueError
        # Generate and return the fraction
        return (numer/denom)
    except ValueError:
        print("Input format 'X/Y' and X,Y are integers")
        return False
    except ZeroDivisionError:
        print("Division by zero not allowed")
        return False


def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
