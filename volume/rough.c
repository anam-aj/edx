// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE *ptr = fopen("volume.c", "r");

    char ch1 = fgetc(ptr);

    printf("%c\n", ch1);

    char ch2 = fgetc(ptr);

    printf("%c\n", ch2);

    fclose(ptr);
}
