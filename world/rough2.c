// Print the the no of minimum coins
#include <cs50.h>
#include <stdio.h>

int check_sum(long number);

int main(void)
{
    long number;
    // Promts the user to enter card no
    do
    {
        number = get_long("Enter Card Number: ");
    }
    while (number <= 0);

    int new = number/10;
    printf("%i\n", new);


}
