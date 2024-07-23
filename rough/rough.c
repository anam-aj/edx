#include <stdio.h>

int main(void)
{
    char *f = "abcd";
    char *f2 = "abcd";

    FILE *file1 = fopen(f, "w");
    FILE *file2 = fopen(f2, "w");

    fclose(file1);
    fclose(file2);

}
