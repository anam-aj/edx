// Program to encrypt msg using caesar cipher

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    string a = "abc";
    printf("%s\n", a);

    a = "pqr";
    printf("%s\n", a);

    string p = "xyz";
    string q = p;
    printf("%s\n", q);

    q = "abc";

    printf("%s\n", p);
    printf("%s\n\n", q);

    char t = q[1];
    printf("%c\n", t);

    q[1] ='k';
    //printf("%s\n", q);

    //string l = q;
    //printf("%s\n", l);





}

