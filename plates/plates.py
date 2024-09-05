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

    # Ensure length is fron 2 to 6(inclusive)
    if len(s) < 2 or len(s) > 6:
        return False

    # Ensure plate contains only numbers and letters
    if not(s.alnum())
        return False

    # Ensure first two character are letter
    if not(s[0].isalpha()) or not(s[1].isalpha()):
        return False



main()
