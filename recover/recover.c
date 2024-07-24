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

    // Open file to recover from, for reading
    FILE *memory_card = fopen(argv[1], "r");
    if (memory_card == NULL)
    {
        return 1;
    }

    // Create name of jpg files
    char name[8];
    int srl_num = 0;
    sprintf(name, "%03i.jpg", srl_num);

    // Buffer to read from memory card
    uint8_t buffer[512];

    // Reads memory card
    while ((fread(buffer, sizeof(uint8_t), 512, memory_card)) != 0)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            FILE *image = fopen(name, "w");
            if (image == NULL)
            {
                return 1;
            }

            (fwrite(buffer, sizeof(uint8_t), 512, image));
            break;
        }
    }

    FILE *image = fopen(name, "a");
    
    while ((fread(buffer, sizeof(uint8_t), 512, memory_card)) != 0)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            fclose(image);
            name++;
            fopen(name, "w");
            (fwrite(buffer, sizeof(uint8_t), 512, image));
        }
        else
        {
            (fwrite(buffer, sizeof(uint8_t), 512, name));
        }
    }
    fclose(name);

    fclose(memory_card);
}
