# Program to simulate coke vending machine


def main():

    # Set cost of coke
    cost = 50
    amount_due = cost

    # Promts user for remaining amount
    while amount_due > 0:

        print(f"Amount Due: {amount_due}")
        coin_value = int(input("Insert Coin: "))
        if coin_value in [5, 10, 25]:
            amount_due -= coin_value

    # Chnage owed
    change = -1 * amount_due
    print(f"Change Owed: {change}")


main()
