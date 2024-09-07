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
    
    valid_date = False
    while not valid_date:

        date = input("Date: ")

        formatted_date = split_on_slash(date)
        if formatted_date:
            print(formatted_date)
            valid_date = True
        else:
            formatted_date = split_on_space(date)
            if formatted_date:
                print(formatted_date)
                valid_date = True


def split_on_slash(date):

    try:
        month, day, year = date.split("/")
    except:
        return False
    else:
        try:
            month, day, year = int(month), int(day), int(year)
            if month < 1 or month > 12 or day < 1 or day > 31:
                raise ValueError
        except:
            return False
        else:
            formatted_date = f"{year:04}-{month:02}-{day:02}"
            return formatted_date


def split_on_space(date):

    try:
        month, day, year = date.split(" ")
    except:
        return False
    else:
        try:
            if month not in months:
                raise KeyError
            if "," not in day:
                raise ValueError
            day, year = int(day.replace(",", "")), int(year)
            if day < 1 or day > 31:
                raise ValueError
        except:
            return False
        else:
            month_count = 0
            for m in months:
                month_count += 1
                if m == month:
                    month = month_count
                    break

    formatted_date = (f"{year:04}-{month:02}-{day:02}")
    return formatted_date


main()
