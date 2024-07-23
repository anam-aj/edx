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

    // Reads file to recover from
    FIlE *memory_card = fopen("argv[1]", "r");



}
