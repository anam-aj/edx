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
    


if __name__ == "__main__":
    main()
