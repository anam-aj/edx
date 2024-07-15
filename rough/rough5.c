// Program to encrypt msg using caesar cipher

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 9
bool locked[MAX][MAX];

int main(void)
{
    //candidate_count = argc - 1
    // Clear graph of locked in pairs
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            locked[i][j] = false;
        }
    }


    for (int v = 0; v < 3; v++)
    {
        for (int vv = 0; vv < 3; vv++)
        {
            printf("%i ", locked[v][vv]);
        }
        printf("\n");
    }
}
