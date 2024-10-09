# Program to tell age in minutes

import re
import sys
import inflect
import operator

from datetime import date


def main():

    # Get date of birth from user
    birth_date = get_date("Enter date of birth: ")

    # Fetch current date
    current_date = date.today()

    # Calculates age 
    age = operator.__sub__(current_date, birth_date)
    total_minutes = (age.days * 24 * 60) + (age.seconds // 60)

    p = inflect.engine()
    age = p.number_to_words(total_minutes)

    print(f"{age.capitalize()} minutes")


# Functions to get valid date object
def get_date(text):

    # Promt user for date
    date = input(text)

    # Ensure birthdate is in YYYY-MM-DD format
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if not re.search(pattern, date):
        sys.exit("Invalid date, correct format: YYYY-MM-DD")

    # Ensure birth date is valid and converts to date-object
    year, month, day = date.split("-")
    try:
        date = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")

    return date


if __name__ == "__main__":
    main()
