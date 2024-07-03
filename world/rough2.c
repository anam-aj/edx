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

    if (change == 11 || change == 10)
    {
        printf("b");
    }

}
