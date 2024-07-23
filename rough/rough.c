#include <stdio.h>

int main(void)
{
    FILE *file = fopen("cs5033.txt", "w");

    fclose(file);

}
