#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{

    char *f = "abcd";
    char f2[4];
    strcpy(f2, f);


    printf("%p\n", f);
    printf("%p\n", f2);

    printf("%s\n", f);
    printf("%s\n", f2);




    //FILE *file1 = fopen(f, "w");
    //FILE *file2 = fopen(f2, "w");

    //fclose(file1);
    //fclose(file2);

}
