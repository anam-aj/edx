// Program to encrypt msg using caesar cipher

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

string fun(string str);

int main(void)
{
    string s = "abc";



    printf("%s\n", fun(s));

}

string fun(string str)
{
    str[1] = 'p';
    return str;
}
