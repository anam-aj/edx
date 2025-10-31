# Program to overlay cs50 shirt on user image

import os
import sys

from PIL import Image, ImageOps


def main():

    validate_arguments()

    # Get command line arguments
    input_img = sys.argv[1]
    output_img = sys.argv[2]

    with open_file(input_img) as user_photo, open_file("shirt.png") as shirt_img:

        # Crops and resize user's photo to match shirt's image
        user_photo = ImageOps.fit(user_photo, (600, 600))
        # Overlay shirt on user photo and save it
        user_photo.paste(shirt_img, shirt_img)
        user_photo.save(output_img)


# Check validity of command line arguments
def validate_arguments():

    # Ensure correct number of comand line argument
    if len(sys.argv) != 3:
        sys.exit("Please give two file name")

    # Ensure name are valid image files
    read_file = ((sys.argv[1]).lower()).endswith((".jpg", ".jpeg", ".png"))
    if not read_file:
        sys.exit("Invalid input")
    write_file = ((sys.argv[2]).lower()).endswith((".jpg", ".jpeg", ".png"))
    if not write_file:
        sys.exit("Invalid output")

    # Ensure both input and output have same extension
    _, input_ext = os.path.splitext(sys.argv[1])
    _, output_ext = os.path.splitext(sys.argv[2])
    if input_ext != output_ext:
        sys.exit("Input and Iutput file must have same type or extension")


# Ensure file exist
def open_file(file_name):

    try:
        return Image.open(file_name)
    except FileNotFoundError:
        sys.exit("file not found")


if __name__ == "__main__":
    main()
