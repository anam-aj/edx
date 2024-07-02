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

    if change >= 25
    // No of Quarters
    int quarters = no_of_coins(change, 25);
    change %= 25

    // No of dimes
    int dimes = no_of_coins(change, 10);
    change %= 10

    // No of nickles
    int nickles = no_of_coins(change, 5);
    change %= 5

    // No of pennies
    int pennies = no_of_coins(change, 1);
}


// Function to calculate no of coins of given value
int no_of_coins(int amount, int coin_value)
{
    int coins = quotient(amount, coin_value);
    return coins;
}


// Function to to return quotient
int quotient(int dividend, int divisor)
{
    int remainder = (dividned % divisor);
    int quotient = (dividend - remainder)/divisor;
    return quotient;
}

