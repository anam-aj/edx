#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Checks no of argument
    if (argc != 2)
    {
        printf("Usage: ./recover file_name\n");
        return 1;
    }

    // Open memory card for reading
    FILE *memory_card = fopen(argv[1], "r");
    if (memory_card == NULL)
    {
        return 1;
    }

    // Create name for jpg file
    char name[8];
    int srl_num = 0;
    sprintf(name, "%03i.jpg", srl_num);

    // Buffer to read from memory card
    uint8_t buffer[512];

    // Create file for first image
    FILE *image = fopen(name, "w");
    if (image == NULL)
    {
        return 1;
    }

    // Reads memory card
    while ((fread(buffer, sizeof(uint8_t), 512, memory_card)) == 512)
    {
        // Write to image file when first image is found in memory card
        // and breaks after writing first 512 byte block
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            (fwrite(buffer, sizeof(uint8_t), 512, image));
            break;
        }
    }

    // Reads memory card and create an new image file whenever a new image
    while ((fread(buffer, sizeof(uint8_t), 512, memory_card)) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            fclose(image);
            srl_num++;
            sprintf(name, "%03i.jpg", srl_num);
            image = fopen(name, "w");
            (fwrite(buffer, sizeof(uint8_t), 512, image));
        }
        else
        {
            (fwrite(buffer, sizeof(uint8_t), 512, image));
        }
    }
    fclose(image);

    fclose(memory_card);
}
