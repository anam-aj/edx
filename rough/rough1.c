#include <stdio.h>

int main(void)
{
    int a;
    a = 2;
    printf("%p\n", &a);
    a = 3;
    printf("%p\n", &a);


    char *namept;
    namept = "xyz";
    printf("%p\n", namept);
    namept = "abcdef";
    printf("%p\n", namept);
    //printf("%s\n", namept);

    char buffer[14];
    int i = 5;
    sprintf(buffer, "This is CS%03i", i);
    printf("%s\n", buffer);
}
