# Program to convert fraction to percentage


def main():

    # Ask user to enter fraction
    fraction = input("Fraction: ")
    numer , denom = fraction.split("/")


    try:
        numer = float(numer)
        denom = float(denom)
    except ValueError:
        print("Enter valid fraction not letters")



main()
