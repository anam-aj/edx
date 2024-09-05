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
    number_found = False

    for ch in remaining_string:
        if ch.isnumeric():
            if ch == "0" and not number_found:
                return False
            else:
                number_found = True
                break

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
