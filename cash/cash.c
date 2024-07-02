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


}


// Function to calculate no of quarters to be given
int no_of_quarters(amount)
{
    int remainder = amount % 25;
    int quarters = (amount - remainder)/25
    
}
