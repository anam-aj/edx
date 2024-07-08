// Program to encrypt msg using caesar cipher

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    //string a = "abc";
    //a[1] = 'k';

    //string a[] = {"abc"};
    //a[0][1] = 'k';

    string a = get_string("s: ");
    a[1] = 'k';


    printf("%s\n", a);

}
