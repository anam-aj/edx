#include <stdio.h>

int main(void)
{
    char *name = "abcd";
    printf("%p\n", name);
    printf("%p\n", &name);
    printf("%p\n", "abcd");

    //name = "xyz";
    //printf("%p\n", name);
    //FILE *file1 = fopen(name, "w");

    //printf("hi\n");


}
