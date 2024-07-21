// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
//const int HEADER_SIZE = 44;

int main(void)
{

    // TODO: Copy header from input file to output file
    FILE *pt = fopen("input.wav", "r");

    //char chr;
    for (int i = 0; i < 10; i++)
    {

       char chr1 = fgetc(pt);
       printf("%c,", chr1);

    }
    printf("\n");

    for (int i = 0; i < 10; i++)
    {

       char chr1 = fgetc(pt);
       printf("%c,", chr1);

    }
    printf("\n");
    // TODO: Read samples from input file and write updated data to output file
    //int16_t chr2;
    //int16_t chr3;
    //while ((fread(&chr2, sizeof(int16_t), 1, input)) != EOF)
    //{
        //chr3 = factor * chr2;
        //fwrite(&chr3, sizeof(int16_t), 1, output);
    //}

    // Close files
    fclose(pt);
}
