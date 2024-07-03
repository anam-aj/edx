// Prints pyramid
#include <cs50.h>
#include <stdio.h>

int no_of_digits(long number);
long quotient(long dividend, int divisor);

int main(void)
{
    long card_number;
    // Promts the user to enter card no
    do
    card_number = get_long("Enter Card Number: ");
    while (card_number <= 0);
}


int no_of_digits(long number)
{
    int digit_count = 0;
    while (number > 0);
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
