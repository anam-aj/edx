// Program to encrypt text using substitution key

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int main(int argc, string argv[])
{
    // Check for no of arguments(only 1) and its length(only 26)
    // if not prints error msg
    if ((argc != 2) || (strlen(argv[1]) != 26))
    {
        printf("Exactly 1 argument, only alphbetical,
                26 character, no repetition"
              );

        return 1;
    }

    else
    {
        // Checks if argument is alphabetical, if not prints error msg
        for (int i = 0; i < 26; i++)
        {
            if (isalpha(argv[1][i]) == 0)
            {
                printf("Exactly 1 argument, only alphbetical,
                        26 character, no repetition"
                      );

                return 1;
            }
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
