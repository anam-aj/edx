#include <stdio.h>

int main(void)
{
    char buffer[13];

    int i = 50;
    sprintf(buffer, "This is CS%03i", i);
    printf("%s\n", buffer);
}
