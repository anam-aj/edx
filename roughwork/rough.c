#include <stdio.h>

int main(void)
{
    char *name = "abcd";
    name = "xyz";
    FILE *file1 = fopen(name, "w");

    printf("hi\n");


}
