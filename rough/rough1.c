// Program to encrypt msg using caesar cipher

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    string s = "abc";

    s[1] = s[1] + 2;

    printf("%s\n", s);

}
