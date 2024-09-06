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
            mon, day, year = date.split("/")
        except:
            pass
        else:
            break
main()
