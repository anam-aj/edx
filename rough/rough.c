#include <stdio.h>

int main(void)
{
    char *f = "abcd";

    FILE *file = fopen(f, "w");

    fclose(file);

}
