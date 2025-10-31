# Program to convert fraction to percentage


def main():

    # Ask user to enter fraction
    while True:
        fraction = input("Fraction: ")
        percent = convert(fraction)
        if percent != None:
            if 0 <= percent <= 100:
                break

    # Print result to user
    print(gauge(percent))


def convert(fraction):

    try:
        numer, denom = fraction.split("/")
        # Ensure both numerator and denominator are integers
        if not numer.isdigit() or not denom.isdigit():
            raise ValueError
        numer, denom = int(numer), int(denom)
        fraction = numer / denom
        # Ensure fraction is not greater than 1
        if numer > denom:
            raise ValueError
    except ValueError:
        print("Input format 'X/Y' and X,Y are integers")
        raise
    except ZeroDivisionError:
        print("Division by zero not allowed")
        raise
    else:
        # Convert to percent
        percent = int(round(fraction * 100))
        return percent


def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
