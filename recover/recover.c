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
    

    fclose(memory_card);


}
