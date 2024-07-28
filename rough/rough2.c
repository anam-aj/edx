#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void change_str(char *p);

int main(void)
{
    char *s = "abc";

    change_str(s);

    printf("%s\n", s);
}

void change_str(char *p)
{
    *p = "xyz";
}

