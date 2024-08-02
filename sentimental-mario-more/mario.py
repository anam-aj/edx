# Program to print

# Funtion import
from cs50 import get_int


def main():

    # Promts user for height
    while True:
        height = get_int("Enter Height: ")
        if height >= 1 and height <= 8:
            break

    # Prints the pyramid with given height
    for r in range(height):
        print_row(height - (r + 1), r + 1)


# Print row
def print_row(spaces, bricks):

    # Print left spaces
    for s in range(spaces):
        print(" ", end="")

    # Print left bricks
    for b in range(bricks):
        print("#", end="")

    # Print centre spaces
    print("  ", end="")

    # Print right bricks
    for b in range(bricks):
        print("#", end="")

    # Move to next line
    print("")


main()
