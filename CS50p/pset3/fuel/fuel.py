# Program to convert fraction to percentage


def main():

    # Ask user to enter fraction
    fraction = input("Fraction: ")
    

    try:
        fraction = float(fraction)
    except ValueError:
        print("Enter valid fraction not letters")



main()
