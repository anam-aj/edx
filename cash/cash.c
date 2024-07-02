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

// Function to calculate quarters
int no_of_quarter(amount)
{
    
}


// Function to to return quotient
int quotient(int dividend, int divisor)
{
    int remainder = (dividned % divisor);
    int quotient = (dividend - remainder)/divisor;
    return quotient;
}

