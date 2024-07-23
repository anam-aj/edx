#include <stdio.h>
#include <cs50.h>

int main(void)
{

    char *f = "abcd";
    char *f2 = "abc";

    printf("%p\n", f);
    printf("%p\n", f2);

    f2 = "abcd";

    printf("%p\n", f);
    printf("%p\n", f2);

    //FILE *file1 = fopen(f, "w");
    //FILE *file2 = fopen(f2, "w");

    //fclose(file1);
    //fclose(file2);

}
