// Program to encrypt msg using caesar cipher

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    // only one command line argument
    // if 0 or more, error msg of choice and return 1
    if (argc != 2)
    {
        printf("Please give exactly 1 argument\n");
        return 1;
    }

    // command line arg should only be decimal digits, a non negaive integr
    // if not print "Usage: ./caesar key", return 1
    else
    {
        for (int i = 0, len = strlen(argv[1]); i < len; i++)
        {
            if (isdigit(argv[1][i]) == 0)
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }

        // user input with get string with two spaces "plaintext:  "
        string plaintext = get_string("plaintext:  ");

        // output  with one space "ciphertext: "
        string ciphertext = cipher_text(plaintext);

        // preserve lowercase and upppercase

        // exit main with 0
    }
}

string cipher_text(string text)
{
    for (int i = 0, len = strlen(text); i < len, i++)
    {
        if ();
    }
}
