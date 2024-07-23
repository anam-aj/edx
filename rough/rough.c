#include <stdio.h>

int main(void)
{
    char *f = "abcd";

    FILE *file1 = fopen(f, "w");
    FILE *file2 = fopen("abcd", "w");

    fclose(file1);
    fclose(file2);

}
