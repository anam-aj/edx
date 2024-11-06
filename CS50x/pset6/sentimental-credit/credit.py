# Programme to check validity and type of card


# Funtion import
from cs50 import get_int


def main():

    # Promts the user to enter card no
    while True:
        card_number = get_int("Enter Card Number: ")
        if card_number > 0:
            break

    # Checks if checksum is correct
    if check_sum(card_number) == 0:

        d1 = first_digit(card_number)
        d2 = first_two_digits(card_number)
        d_num = no_of_digits(card_number)

        # Checks criteria for American Express
        if (d_num == 15) and (d2 == 34 or d2 == 37):

            print("AMEX")

        # Checks criteria for MasterCard
        elif (d_num == 16) and (d2 > 50 and d2 < 56):

            print("MASTERCARD")

        # Checks criteria for Visa
        elif (d_num == 13 or d_num == 16) and (d1 == 4):

            print("VISA")

        else:
            print("INVALID")

    else:
        print("INVALID")


# Function to give first digit of the given number
def first_digit(number):

    while no_of_digits(number) > 1:
        number = number // 10

    return number


# Function to give first two digits of the given number
def first_two_digits(number):

    while no_of_digits(number) > 2:
        number = (number // 10)

    return number


# Function to calculate no of digits in the given number
def no_of_digits(number):

    digit_count = 0
    while (number > 0):
        digit_count += 1
        number = (number // 10)

    return digit_count


# Defining checksum according to lunh alogrithm
def check_sum(number):

    sum_of_even_place_digits = 0
    sum_of_odd_place_digits = 0

    while (number > 0):

        digit_at_odd_place = number % 10
        sum_of_odd_place_digits += digit_at_odd_place
        number = (number // 10)

        digit_at_even_place = number % 10
        twice = (2 * digit_at_even_place)

        if (twice > 0):
            unitdigit = (twice % 10)
            sum_of_even_place_digits += unitdigit
            tensdigit = (twice // 10)
            sum_of_even_place_digits += tensdigit

        number = (number // 10)

    net_sum = (sum_of_odd_place_digits) + (sum_of_even_place_digits)
    unit_digit = net_sum % 10

    return unit_digit


main()
