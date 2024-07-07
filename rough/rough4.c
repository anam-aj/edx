
#include <stdio.h>
#include <cs50.h>
int main(void)
{
    string s = "abc";
    string str = s;
    s[2] = 'p';
    printf("%s\n", s);
}
