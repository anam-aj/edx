
#include <stdio.h>
#include <cs50.h>
int main(void)
{
    char s[] = {'a','b','c'};
    s[2] = 'p';

    printf("%c \n", s[2]);
}
