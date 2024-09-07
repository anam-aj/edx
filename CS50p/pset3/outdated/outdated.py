# Program to covert date to standard format

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():

    # Ensure date is of valid format
    valid_date = False
    while not valid_date:

        # Promts user for date
        date = input("Date: ")

        # Print result when date is given as "MM/DD/YYYY"
        formatted_date = split_on_slash(date)
        if formatted_date:
            print(formatted_date)
            valid_date = True
        else:
            # Print result when date is given as "Month Day, Year"
            formatted_date = split_on_space(date)
            if formatted_date:
                print(formatted_date)
                valid_date = True


# Convert to standard format from "MM/DD/YYYY"
def split_on_slash(date):

    try:
        month, day, year = date.split("/")
    except:
        return False
    else:
        try:
            # Ensure month, day, year are integers
            month, day, year = int(month), int(day), int(year)
            # Ensure month and day are valid
            if month < 1 or month > 12 or day < 1 or day > 31:
                raise ValueError
        except:
            return False
        else:
            formatted_date = f"{year:04}-{month:02}-{day:02}"
            return formatted_date


# Convert to standard format from "Month Day, Year"
def split_on_space(date):

    try:
        month, day, year = date.split(" ")
    except:
        return False
    else:
        try:
            # Ensure month is valid
            if month not in months:
                raise KeyError
            if "," not in day:
                raise ValueError
            day, year = int(day.replace(",", "")), int(year)
            # Ensure day is valid
            if day < 1 or day > 31:
                raise ValueError
        except:
            return False
        else:
            # Covert "month-name" to "month-number"
            month_count = 0
            for m in months:
                month_count += 1
                if m == month:
                    month = month_count
                    break

            formatted_date = (f"{year:04}-{month:02}-{day:02}")
            return formatted_date


main()
