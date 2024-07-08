// Program to encrypt text using substitution key

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// exactly 1 command line argument i.e. key,
// if less than1 or more, print error msg of chioce,
// return 1 from main immediately

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Exactly 1 argument, only alphbetical,
                26 character, no repetition"
              );

        return 1;
    }

    // key has exactly 26 character
    // return 1 from main immediately
    else if (strlen(argv[1]) != 26)
    {
        printf("Exactly 1 argument, only alphbetical,
                26 character, no repetition"
              );

        return 1;
    }

    // only alphabetical
    // return 1 from main immediately
    else
    {
        for (int i = 0; i < 26; i++)
        {
            if ( )
        }
    }

        // each letter only once, if not then error msg of choice
        // return 1 from main immediately

}



// key should be case insensitive

// promt user for plaintext with "plaintext: "
// one sapce without new line

// output ciphertest with "ciphertext:  "
// two spaces without new line
// in output only alphabetical letters change rest unchanged
// output must preserve case, uppercase and lowercase

// after output, newline,exit by return 0 from main
