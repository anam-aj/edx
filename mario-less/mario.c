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

    for (int r = 1; r <= height; r++)
    {
        print_row(height - r, r);
    }
}

void print_row(int spaces, int bricks)
{
    for (int j = 1; j <= spaces; j++)
    {
        printf(" ");
    }
    for (int i = 1; i <= bricks; i++)
    {
        printf("#");
    }
    printf("\n");
}
