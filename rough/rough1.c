#include <stdio.h>

int main(void)
{
    char *namept;
    namept = "xyz";
    namept = "abcdef";
    printf("%s\n", namept);

    char *buffer;
    buffer = "qwe";
    int i = 50;
    sprintf(buffer, "This is CS%i", i);
    printf("%s\n", buffer);
}
