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

    char buffer[13];
    int i = 50;
    sprintf(buffer, "This is CS%i", i);
    printf("%s\n", buffer);
}
