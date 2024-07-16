#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string s1 = "abc";
    char s2[3] = {'a', 'b', 'c'};

    printf("%c /n", s1[1]);
    printf("%c /n", s2[1]);

    //s1[1] = 'x';
    s2[1] = 'x';

    printf("%c /n", s1[1]);
    printf("%c /n", s2[1]);



}
