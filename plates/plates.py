# Program to check validity of plate


def main():

    # Promt user for plate
    plate = input("Plate: ")

    # Check and print validity status
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# Determine validity of plate
def is_valid(s):

    # Check length
    if len(s) < 2 or len(s) > 6:
        



main()
