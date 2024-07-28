#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

string change_str(string p);

int main(void)
{
    string s = "abc";

    change_str(s);

    printf("%s\n", s);
}

string change_str(string p)
{
    p = "xyz";
    return p;
}

