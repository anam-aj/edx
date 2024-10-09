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

    # Calculate age in minutes
    age = operator.__sub__(current_date, birth_date)
    total_minutes = (age.days * 24 * 60) + (age.seconds // 60)

    # Convert age to words and prints to user
    p = inflect.engine()
    age = p.number_to_words(total_minutes, andword=""   )
    print(f"{age.capitalize()} minutes")


# Functions to get valid date object
def get_date(text):

    # Promt user for date
    user_date = input(text)

    # Ensure birthdate is in YYYY-MM-DD format
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if not re.search(pattern, user_date):
        sys.exit("Invalid date, correct format: YYYY-MM-DD")

    # Ensure birth date is valid and converts to date-object
    year, month, day = user_date.split("-")
    try:
        user_date = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")

    return user_date


if __name__ == "__main__":
    main()
