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

// function to give first two digits of the given number
int first_two_digits(long number)
{
    while (no_of_digits(number) > 2)
    {
        number = quotient(number);
    }
    return number;
}


// function to calculate no of digits
int no_of_digits(long number)
{
    int digit_count = 0;
    while (number > 0)
    {
        digit_count++ ;
        number = quotient(number, 10);
    }

    return digit_count;
}


// peter_lunh_sum means sum of digits according to Lunh's algorithm
int peter_lunh_sum(long number)
{
    int sum_of_even_place_digits = 0;
    int sum_of_odd_place_digits = 0;

    while (number > 0)
    {
        int digit_at_odd_place = number % 10;
        sum_of_odd_place_digits += digit_at_odd_place;
        number = quotient(number, 10);

        int digit_at_even_place = number % 10;
        sum_of_even_place_digits += digit_at_even_place;
        number = quotient(number, 10);
    }

    int peter_lunh_sum = (sum_of_odd_place_digits) + (2 * sum_of_even_place_digits);
    return peter_lunh_sum;
}


// Function to to return quotient(with out decimal part)
long quotient(long dividend, int divisor)
{
    int remainder = (dividend % divisor);
    long quotient = (dividend - remainder) / divisor;
    return quotient;
}
