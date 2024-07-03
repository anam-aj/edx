// Programme to check validity and type of card
#include <cs50.h>
#include <stdio.h>

int check_sum(long number);
int no_of_digits(long number);
long first_digit(long number);
long first_two_digits(long number);

int main(void)
{
    long card_number;
    // Promts the user to enter card no
    do
    {
        card_number = get_long("Enter Card Number: ");
    }
    while (card_number <= 0);

    if ((check_sum(card_number)) == 0)
    {
        if ((no_of_digits(card_number) == 15) &&
            (first_two_digits(card_number) == 34 || first_two_digits(card_number) == 37))
        {
            printf("AMEX\n");
        }

        else if ((no_of_digits(card_number) == 16) &&
                 (first_two_digits(card_number) > 50 && first_two_digits(card_number) < 56))
        {
            printf("MASTERCARD\n");
        }

        else if ((no_of_digits(card_number) == 13 || no_of_digits(card_number) == 16) &&
                 (first_digit(card_number) == 4))
        {
            printf("VISA\n");
        }
    }

    else
    {
        printf("INVALID\n");
    }
}

// function to give first digit of the given number
long first_digit(long number)
{
    while (no_of_digits(number) > 1)
    {
        number = (number / 10);
    }
    return number;
}

// function to give first two digits of the given number
long first_two_digits(long number)
{
    while (no_of_digits(number) > 2)
    {
        number = (number / 10);
    }
    return number;
}

// function to calculate no of digits
int no_of_digits(long number)
{
    int digit_count = 0;
    while (number > 0)
    {
        digit_count++;
        number = (number / 10);
    }
    return digit_count;
}

// Defining checksum according to lunh alogrithm
int check_sum(long number)
{
    int sum_of_even_place_digits = 0;
    int sum_of_odd_place_digits = 0;

    while (number > 0)
    {
        int digit_at_odd_place = number % 10;
        sum_of_odd_place_digits += digit_at_odd_place;
        number = (number / 10);

        int digit_at_even_place = number % 10;
        sum_of_even_place_digits += digit_at_even_place;
        number = (number / 10);
    }

    int net_sum = (sum_of_odd_place_digits) + (2 * sum_of_even_place_digits);
    int unit_digit = net_sum % 10;
    return unit_digit;
}
