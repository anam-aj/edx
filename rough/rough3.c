// Program to encrypt msg using caesar cipher

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int preferences[9][9];

int main(void)
{
    int preferences[9][9];

    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            preferences[i][j] = 0;
        }
    }


    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            printf("%i ", preferences[i][j]);
        }
        printf("\n");
    }

}
