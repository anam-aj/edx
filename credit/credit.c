// Programme to check validity and type of card
#include <cs50.h>
#include <stdio.h>

long quotient(long dividend, int divisor);
int checksum(long number);

int main(void)
{
    long card_number;
    // Promts the user to enter card no
    do
    card_number = get_long("Enter Card Number: ");
    while (card_number <= 0);
}


// defining Checksum
int checksum(long number)
{
    int sum_of_even_place_digits = 0;
    int sum_of_odd_place_digits = 0;

    while (number > 0);
    {
        int digit_at_odd_place = number % 10;
        sum_of_odd_place_digits += digit_at_odd_place;
        quotient(number, 10);

        int digit_at_even_place = number % 10;
        sum_of_even_place_digits += digit_at_even_place;
        quotient(number, 10);
    }

    int sum_of_all_digits = (sum_of_odd_place_digits + sum_of_odd_place_digits);
    return sum_of_all_digits;
}


// Function to to return quotient(with out decimal part)
long quotient(long dividend, int divisor)
{
    int remainder = (dividend % divisor);
    long quotient = (dividend - remainder) / divisor;
    return quotient;
}
