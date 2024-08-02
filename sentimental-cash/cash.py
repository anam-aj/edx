# Print the minimum no of coins

# Funtion import
from cs50 import get_float


def main()

    while True:
        change = get_float("Change owed: ")
        if change < 0:
            break
    dollars = change / 1
    cents =

    # No of Quarters
    int quarters = no_of_coins(change, 25)

    # Remaining change
    change %= 25

    # No of dimes
    int dimes = no_of_coins(change, 10)

    change %= 10

    # No of nickles
    int nickles = no_of_coins(change, 5)

    change %= 5

    # No of pennies
    int pennies = no_of_coins(change, 1)

    int total_coins = (quarters + dimes + nickles + pennies)

    printf("%i\n", total_coins)


// Function to calculate no of coins of given value
int no_of_coins(int amount, int coin_value)
{
    int coins = (amount / coin_value);
    return coins;
}
