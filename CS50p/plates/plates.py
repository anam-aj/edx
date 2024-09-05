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

    # Remaining string after first two letters
    remaining_string = s[2:]

    # Variable to track first encounter of number
    number_found = False

    # Goes through each character of remaining string
    for ch in remaining_string:

        # When character is numeric
        if ch.isnumeric():
            # Ensure first number is not "0"
            if ch == "0" and not number_found:
                return False
            # Update that first number is encountered(so further number can be "0")
            number_found = True

        # Ensure that all character following first number are numeric
        # (when character is not numeric)
        elif number_found:
            return False


    # Remaining string after first number
    last_string = remaining_string[(count + 1):]

    if number_found:
        if last_string.isnumeric():
            return True
        else:
            return False
    else:
        return True


main()
