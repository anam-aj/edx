// Program to encrypt msg using caesar cipher

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    int list[6] = {2,5,4,1,9,6};

    for (int i = 0; i < 6; i++)
    {
        printf("%i, ", list[i]);
    }
    printf("\n");



    for (int i = 0; i < 6; i++)
    {
        for (int j = 0; j < 6; j++)
        {
            if (list[i] < list[i + 1])
            {
                int temp = list[i];
                list[i] = list[i + 1];
                list[i + 1] = temp;
            }
        }

    }

    

    for (int i = 0; i < 6; i++)
    {
        printf("%i, ", list[i]);
    }
    printf("\n");


}
