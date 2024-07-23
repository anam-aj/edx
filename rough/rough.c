#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{

    char *f = "abcd";
    char f2[5];
    strcpy(f2, f);

    printf("%p\n", f);
    printf("%p\n", f2);

    printf("%s\n", f);
    printf("%s\n", f2);


    FILE *file1 = fopen("abcd", "w");
    fclose(file1);
    FILE *file2 = fopen("abcd", "w");


    printf("%p\n", file1);
    printf("%p\n", file2);

    //fclose(file1);
    fclose(file2);

    printf("%p\n", file1);
    printf("%p\n", file2);

}
