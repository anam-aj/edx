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

    uint8_t buffer[512];
    while ((fread(buffer, sizeof(uint8_t), 512, memory_card)) != 0)
    {
        if (buffer[0] == 0xff && buffer[0] == 0xd8 && buffer[0] == 0xff && buffer[0] == 0xff)
    }

    fclose(memory_card);


}
