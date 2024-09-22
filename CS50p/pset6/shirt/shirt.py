# Program to overlay cs50 shirt on user image

import PIL
import sys


def main():

    validate_arguments()

    # Get command line arguments
    read_file = sys.argv[1]
    write_file = sys.argv[2]

    with open_file(read_file) as user_photo, open_file("shirt.png") as shirt_img:

        shirt = PIL.ImageOps.fit(shirt, (600, 600))


# Check validity of command line arguments
def validate_arguments():

    # Ensure correct number of comand line argument
    if len(sys.argv) != 3:
        sys.exit("Please give two file name")

    # Ensure name are valid image files
    read_file = (sys.argv[1]).lower().endswith(".jpg", ".jpeg", ".png")
    write_file = (sys.argv[2]).lower().endswith(".jpg", ".jpeg", ".png")
    if not read_file or not write_file:
        sys.exit("Please enter image file")


# Ensure file exist
def open_file(file_name):

    try:
        return PIL.Image.open(file_name)
    except FileNotFoundError:
        sys.exit("file not found")


if __name__ == "__main__":
    main()
