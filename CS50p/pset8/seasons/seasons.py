# Program to tell age in minutes

import re
import sys

from datetime import date



def main():

    # Promt user for birthdate
    birthdate = input("Enter birthdate: ")

    # Ensure birthdate is in YYYY-MM-DD format
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if not re.search(pattern, birthdate):
        sys.exit("birthdate format: YYYY-MM-DD")
    year, month, day = birthdate.split("-")
    birth_date =
    current_date = date.today

    age = __sub__()



if __name__ == "__main__":
    main()
