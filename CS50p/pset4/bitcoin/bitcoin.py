# Program to tell the cost of given number of bitcoins

import requests
import sys


def main():

    if argv_is_valid():
        num_of_coin = float(sys.argv[1])

        total = num_of_coin * bitcoin_rate()


def argv_is_valid():

    if len(sys.argv) != 2:
        sys.exit("Please give number of bitcoin")

    num = sys.argv[1]
    try:
        num = float(num)
    except:
        sys.exit("Enter a valid number")
    else:
        return True


def bitcoin_rate():

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except:
        sys.exit("Unable to fetch coin details")

    json_obj = response.json()
    rate = float(json_obj["bpi"][USD][rate])



main()
