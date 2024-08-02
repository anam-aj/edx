# Program to print half-pyramid

from cs50 import get_int

def main()

    # Promts user for height
    while True:
        height = get_int("Enter Height: ")
        if height >= 0 and height <= 8:
            break

# Print row of bricks(right aligned)
def print_row(int spaces, int bricks)
{
    // Print spaces
    for (int j = 0; j < spaces; j++)
    {
        printf(" ");
    }

    // Print bricks
    for (int i = 0; i < bricks; i++)
    {
        printf("#");
    }

    printf("\n");
}
