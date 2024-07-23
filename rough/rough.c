#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{

    char *f = "abcd";
    char f2[5] = {'a', 'b', 'c', 'd', '\0'};

    FILE *file1 = fopen(f2, "r");
    fclose(file1);


}
