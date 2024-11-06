# Program to tell meal type


def main():

    # Promts user for time
    time = input("Please Enter Time: ")

    # Convert time to decimal format
    time = convert(time)

    # Get meal type
    meal = meal_type(time)

    # Prints meal type to user
    print(meal)


def convert(time):

    hour, min = time.split(":")
    hour = float(hour)
    min = float(min)
    decimal_time = hour + (min / 60)

    return decimal_time


def meal_type(time):

    if 7 <= time <= 8:
        return "breakfast time"

    elif 12 <= time <= 13:
        return "lunch time"

    elif 18 <= time <= 19:
        return "dinner time"


if __name__ == "__main__":
    main()
