// Print the the no of minimum coins

#include <cs50.h>
#include <stdio.h>

int no_of_coins(int amount, int coin_value);

int main(void)
{
    int change;
    do
    {
        change = get_int("Change owed: ");
    }
    while (change < 0);

    // No of Quarters
    int quarters = no_of_coins(change, 25);

    // Remaining change
    change %= 25;

    // No of dimes
    int dimes = no_of_coins(change, 10);

    change %= 10;

    // No of nickles
    int nickles = no_of_coins(change, 5);

    change %= 5;

    // No of pennies
    int pennies = no_of_coins(change, 1);

    int total_coins = (quarters + dimes + nickles + pennies);

    printf("%i\n", total_coins);
}

// Function to calculate no of coins of given value
int no_of_coins(int amount, int coin_value)
{
    int coins = (amount / coin_value);
    return coins;
}
