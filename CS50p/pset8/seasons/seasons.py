# Program to tell age in minutes

import re
import sys
import inflect
import operator

from datetime import date


def main():

    # Promt user for birthdate
    birthdate = input("Enter birthdate: ")

    # Ensure birthdate is in YYYY-MM-DD format
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if not re.search(pattern, birthdate):
        sys.exit("Invalid date, correct format: YYYY-MM-DD")

    year, month, day = birthdate.split("-")
    try:
        birth_date = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")
    current_date = date.today()

    age = operator.__sub__(birth_date, current_date)
    total_minutes = (age.days * 24 * 60) + (age.seconds // 60)

    p = inflect.engine()
    age = p.number_to_words(total_minutes)

    print(age)


if __name__ == "__main__":
    main()
