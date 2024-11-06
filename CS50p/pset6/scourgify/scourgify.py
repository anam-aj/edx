# Program to reformat and save data into new file

import csv
import sys

from tabulate import tabulate


def main():

    validate_arguments()

    # Get command line arguments
    read_file = sys.argv[1]
    write_file = sys.argv[2]

    with open_file(read_file) as input, open(write_file, "w") as output:
        reader = csv.DictReader(input)

        # Write Headers
        writer = csv.DictWriter(output, fieldnames=["first", "last", "house"])
        writer.writeheader()

        # Write rows or contents
        for row in reader:
            last_name, first_name = row["name"].split(",")
            first_name, last_name = first_name.strip(), last_name.strip()
            writer.writerow(
                {
                    "first": first_name,
                    "last": last_name,
                    "house": row["house"]
                }
            )


# Check validity of command line arguments
def validate_arguments():

    # Ensure correct number of comand line argument
    if len(sys.argv) != 3:
        sys.exit("Please give one and only one file name")

    # Ensure name are valid CSV files
    read_file = (sys.argv[1]).endswith(".csv")
    write_file = (sys.argv[2]).endswith(".csv")
    if not read_file or not write_file:
        sys.exit("Please enter valid csv file")


# Ensure file exist
def open_file(file_name):

    try:
        return open(file_name)
    except FileNotFoundError:
        sys.exit("file not found")


if __name__ == "__main__":
    main()
