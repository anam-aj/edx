#include <stdio.h>

int main(void)
{
    char *namept;
    namept = "xyz";
    printf("%s\n", namept);

    char name[] = {'a','b','c','\0'};
    printf("%s\n", name);

    char buffer[13];

    int i = 50;
    sprintf(buffer, "This is CS%i", i);
    printf("%s\n", buffer);
}
