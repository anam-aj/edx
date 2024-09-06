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
    while True:
        date = input("Date: ")

        split_on_slash = False
        split_on_space = False

        try:
            month, day, year = date.split("/")
        except:
            pass
        else:
            try:
                month, day, year = int(month), int(day), int(year)
            except:
                pass
            else:
                split_on_slash = True
                break

        try:
            month, day, year = date.split(" ")
        except:
            pass
        else:
            try:
                if month not in months:
                    raise KeyError
                day, year = int(day), int(year)
            except:
                pass
            else:
                split_on_space = True
                break

    if split_on_slash:
        print(f"{year:04}-{month:02}-{day:02}")
    elif split_on_space:
        

main()
