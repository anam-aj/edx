# Program to tell age in minutes

import inflect
import operator
import re
import sys

from datetime import date


def main():

    # Get date of birth from user
    birth_date = input("Enter date of birth: ")

    # Check format: YYYY-MM-DD
    if check_date_format(birth_date) == False:
        sys.exit("Invalid format, correct usage: YYYY-MM-YY")

    # Check validity, i.e. day-month-year are permissible values
    if not date_object(birth_date):
        sys.exit("Invalid date")

    birth_date = date_object(birth_date)

    # Fetch current date
    current_date = date.today()

    age_minutes = age_in_minutes(current_date, birth_date)

    # Convert age to words and prints to user
    p = inflect.engine()
    age = p.number_to_words(age_minutes, andword="")
    print(f"{age.capitalize()} minutes")


# Ensure birthdate is in YYYY-MM-DD format
def check_date_format(user_date):

    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if re.search(pattern, user_date):
        return True
    else:
        return False

# Functions to get valid date object


def date_object(user_date):

    try:
        year, month, day = user_date.split("-")
        user_date = date(int(year), int(month), int(day))
    except ValueError:
        return False

    return user_date


# Function to calculate age in minutes
def age_in_minutes(current_date, birth_date):
    age = operator.__sub__(current_date, birth_date)
    age_in_minutes = (age.days * 24 * 60) + (age.seconds // 60)

    return age_in_minutes


if __name__ == "__main__":
    main()
