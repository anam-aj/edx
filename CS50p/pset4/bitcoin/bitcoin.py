# Program to tell the cost of given number of bitcoins

import requests
import sys


def main():

    if argv_is_valid():
        number =  sys.argv[1]

def argv_is_valid():

    if len(sys.argv) != 2:
        sys.exit("Please give number of bitcoin")

    num_of_bitcoin = sys.argv[1]
    try:
        num_of_bitcoin = float(num_of_bitcoin)
    except:
        sys.exit("Enter a valid number")


main()
