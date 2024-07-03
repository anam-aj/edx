// Programme to check validity and type of card
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long number;
    do
    number = get_long("Enter Card Number: ");
    while (number <= 0);
}
