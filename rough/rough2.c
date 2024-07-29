#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *change_str(char *p);

int main(void)
{
    char *s = "abc;
    s = "pqr";

    change_str(s);

    printf("%s\n", s);
}

char *change_str(char *p)
{
    p = "xyz";
    return p;
}
