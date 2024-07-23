#include <stdio.h>

int main(void)
{
    char buffer[14];

    int i = 1;
    sprintf(buffer, "This is CS%03i", i);
    printf("%s\n", buffer);
}
