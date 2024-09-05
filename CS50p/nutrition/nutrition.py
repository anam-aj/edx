# program to print calorie content of food


def main():




main()







def main():
    # Prompt user for plate
    plate = input("Plate: ")

    # Check and print validity status
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Determine validity of plate
def is_valid(s):
    # Ensure length is from 2 to 6 (inclusive)
    if len(s) < 2 or len(s) > 6:
        return False

    # Ensure plate contains only numbers and letters
    if not s.isalnum():
        return False

    # Ensure first two characters are letters
    first_two_chr = s[0:2]
    if not first_two_chr.isalpha():
        return False

    # Check that all characters after the first two follow numerical rules
    remaining_string = s[2:]
    number_found = False

    for ch in remaining_string:
        if ch.isnumeric():
            # Ensure first number is not "0"
            if ch == "0" and not number_found:
                return False
            # Update that first number is encountered (so further numbers can be "0")
            number_found = True

        # Ensure that all characters following the first number are also numbers
        elif number_found:
            return False

    return True

main()
