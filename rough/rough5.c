// Program to encrypt msg using caesar cipher

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    int list[6] = {20,5,47,1,9,6};

    for (int i = 0; i < 6; i++)
    {
        printf("%i, ", list[i]);
    }
    printf("\n");



    for (int i = 0; i < 6; i++)
    {
        for (int j = 0; j < 6 - 1; j++)
        {
            if (list[j] < list[j + 1])
            {
                int temp = list[j];
                list[j] = list[j + 1];
                list[j + 1] = temp;
            }
        }

    }



    for (int i = 0; i < 6; i++)
    {
        printf("%i, ", list[i]);
    }
    printf("\n");


}
