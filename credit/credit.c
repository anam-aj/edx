// Programme to check validity and type of card
#include <cs50.h>
#include <stdio.h>

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
    int sum_of_even_digits = 0;
    int sum_of_odd_digits = 0;
    while (number > 0);
    {
        int no_at_odd_place = number % 10;
        sum_of_odd_digits += no_at_odd_place;
        number

    }

}

// Function to to return quotient with out decimal part
int quotient(int dividend, int divisor)
{
    int remainder = (dividend % divisor);
    int quotient = (dividend - remainder) / divisor;
    return quotient;
}
