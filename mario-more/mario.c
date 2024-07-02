// Prints right-aligned pyramid
#include <cs50.h>
#include <stdio.h>

void print_row(int spaces, int bricks);

int main(void)
{
    // Promt the user for pyramid height
    int height;
    do
    {
        height = get_int("Please enter the height: ");
    }
    while (height < 1);

    // prints the pyramid with given height
    for (int r = 0; r < height; r++)
    {
        print_row(height - (r + 1), r + 1);
    }
}

// Print row of bricks(right aligned)
void print_row(int spaces, int bricks)
{
    // Print left spaces
    for (int j = 0; j < spaces; j++)
    {
        printf(" ");
    }

    // Print left bricks
    for (int i = 0; i < bricks; i++)
    {
        printf("#");
    }

    // Print centre spaces
    printf("  ");

    // Print right bricks
    for (int i = 0; i < bricks; i++)
    {
        printf("#");
    }

    printf("\n")

}
