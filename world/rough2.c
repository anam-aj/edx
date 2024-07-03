// Prints pyramid
#include <cs50.h>
#include <stdio.h>


int main(void)
{
    long card_number;
    do
    {
    card_number = get_long("Enter Card Number: ");
    }
    while (card_number <= 0);

    long quotient = card_number/3;

    printf("%li\n", quotient);

}
