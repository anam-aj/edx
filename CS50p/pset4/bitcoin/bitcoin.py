# Program to tell the cost of given number of bitcoins

import requests
import sys


def main():

    if argv_is_valid():

        # Get number of bitcoin
        num_of_coin = float(sys.argv[1])

        # Calculate total value
        total = num_of_coin * bitcoin_rate()

        # Print result to user
        print(f"${total:,.4f}")


# Function to check validity of command line arguments
def argv_is_valid():

    # Checks number of arguments
    if len(sys.argv) != 2:
        sys.exit("Please give number of bitcoin")

    # Ensure argument is a number
    num = sys.argv[1]
    try:
        num = float(num)
    except:
        sys.exit("Enter a valid number")
    else:
        return True


# Funtion to get current bitcoin rate
def bitcoin_rate():

    # Querry API
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except:
        sys.exit("Unable to fetch coin details")

    # Obtain rate from json file
    json_obj = response.json()
    rate = json_obj["bpi"]["USD"]["rate_float"]

    return rate


main()
