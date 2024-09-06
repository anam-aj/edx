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
                break

        
main()
