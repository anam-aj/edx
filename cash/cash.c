// Print the the no of minimum coins
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int change;
    do
    {
        change = get_int("Change owed: ");
    }
    while (change < 0);

    int quarter = 0;
    while (change >= 25);
    {
        change -= 25
        quarter++
    }

    while (change >= 10);
    {
        change -= 10
        number++
    }

}
