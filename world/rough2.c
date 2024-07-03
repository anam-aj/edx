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
}
