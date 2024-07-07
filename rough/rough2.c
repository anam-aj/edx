// Program to encrypt msg using caesar cipher

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function decalration
string ciphertext(string plaintext);
int isstrdigit(string str);

int main(int argc, string argv[])
{
    string s = "a1n";

    //int in = atoi(s[1]);

    //printf("%i\n", in);
    //printf("%s\n", s[1]);

    char str = s[1];
    printf("%c\n", str);
    printf("%c\n", s[1]);

    str = 'o';

    printf("%c\n", str);
    printf("%c\n", s[1]);

}
