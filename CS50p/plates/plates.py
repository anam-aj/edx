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
    if not(s.isalnum()):
        return False

    # Ensure first two character are letter
    first_two_chr = s[0:2]
    if not(first_two_chr.isalpha()):
        return False

    # Ensure validity of remaining string
    remain_chr = s[2:len(s)]
    count = 0

    for ch in remain_chr:
        count
        if ch.isnumeric():
            if ch == "0":
                return False
            else:
                break
        elif


main()
