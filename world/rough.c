// Prints pyramid
#include <cs50.h>
#include <stdio.h>

int no_of_digits(long number);
long quotient(long dividend, int divisor);
int peter_lunh_sum(long number);
long first_two_digits(long number);

int main(void)
{
    long card_number;
    do
    {
    card_number = get_long("Enter Card Number: ");
    }
    while (card_number <= 0);

    printf("%i\n", no_of_digits(card_number));
    printf("%i\n", peter_lunh_sum(card_number));
    printf("%i\n", first_two_digits(card_number));
}

// peter_lunh_sum means sum according to Lunh's algorithm
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


// function to give first two digits of the given number
int first_two_digits(long number)
{
    while (no_of_digits(number) > 2)
    {
        number = quotient(number, 10);
    }
    int number2 = number/1;
    return (number2);
}


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


long quotient(long dividend, int divisor)
{
    int remainder = (dividend % divisor);
    long quotient = (dividend - remainder) / divisor;
    return quotient;
}
