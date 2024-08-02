# Proagrame to calculate minimum no of coins

# Funtion import
from cs50 import get_float


# Calculate minimum no of coins and prints it
def main():

    while True:
        change = get_float("Change owed: ")
        if change > 0:
            break

    dollars = (change // 1) * 100
    cents = (change % 1) * 100
    change = (dollars + cents)

    # No of Quarters
    quarters = no_of_coins(change, 25)
    change %= 25

    # No of dimes
    dimes = no_of_coins(change, 10)
    change %= 10

    # No of nickles
    nickles = no_of_coins(change, 5)
    change %= 5

    # No of pennies
    pennies = no_of_coins(change, 1)

    # Calculate total coins and print it
    total_coins = int(quarters + dimes + nickles + pennies)
    print(total_coins)


# Function to calculate no of coins of given value
def no_of_coins(amount, coin_value):

    coins = (amount // coin_value)
    return coins


main()
