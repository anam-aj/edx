# Program to print half-pyramid

from cs50 import get_int


def main():

    # Promts user for height
    while True:
        height = get_int("Enter Height: ")
        if height >= 0 and height <= 8:
            break

    # Prints the pyramid with given height
    for r in range(height):
        print_row(height - (r + 1), r + 1)


# Print row of bricks(right aligned)
def print_row(spaces, bricks):

    # Print spaces
    for s in range(spaces):
        print(" ")

    # Print bricks
    for b in range(bricks):
        print("#")

    print("")

main()

