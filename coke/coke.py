# Program to simulate coke vending machine


def main():

    # Set cost of coke
    cost = 50
    amount_due = cost

    # Promts user for remaining amount
    while cost > 0:

        print(f"Amount Due: {amount_due}")
        coin_value = int(input("Insert Coin: "))

