# Program to simulate coke vending machine


def main():

    # Set cost of coke
    cost = 50
    amount_due = cost

    # While there is still amount due
    while amount_due > 0:

        # Shows due amount and ask for coin
        print(f"Amount Due: {amount_due}")
        coin_value = int(input("Insert Coin: "))

        # Ensure coin is of valid denomination
        if coin_value in [5, 10, 25]:

            # Update due amount
            amount_due -= coin_value

    # Shows change
    change = -1 * amount_due
    print(f"Change Owed: {change}")


main()
