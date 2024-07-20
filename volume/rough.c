// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE *ptr = fopen("volume.c", "r");

    char ch;
    while ((ch = fgetc(ptr)) != 'e')
    {
        printf("%c,\n", ch);
    }

    //for (int i = 1; i < 44; i++)
    //{
        //printf("%c,\n", fgetc(ptr));
    //}

    //printf("\n");

    //char ch1 = fgetc(ptr);

    //printf("%c\n", fgetc(ptr));

    //char ch2 = fgetc(ptr);

    //printf("%c\n", ch2);

    fclose(ptr);
}
