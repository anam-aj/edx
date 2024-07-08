// Program to encrypt text using substitution key

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function declaration
char is_rep(string word);


int main(int argc, string argv[])
{
    // Check for no of arguments(only 1) and its length(only 26)
    // if not prints error msg
    if ((argc != 2) || (strlen(argv[1]) != 26))
    {
        printf("Give only 1 argument, 26 alphabets, no repetition");

        return 1;
    }

    // Checks if argument is only alphabetical and for repetition
    // prints error msg accordingly
    if ((is_str_alpha(argv[1]) == 'n') || (is_rep(argv[1]) == 'y'))
    {
        printf("Give only 1 argument, 26 alphabets, no repetition");

        return 1;
    }


// promt user for plaintext with "plaintext: "
// one sapce without new line

// output ciphertest with "ciphertext:  "
// two spaces without new line
// in output only alphabetical letters change rest unchanged
// output must preserve case, uppercase and lowercase

// after output, newline,exit by return 0 from main

}

// Function to check if string is alphabetical
// return 'y' if string has only alphabet else return 'n'
char is_str_alpha(string word)
{
    for (int i = 0; i < 26; i++)
    {
        if (isalpha(argv[1][i]) == 0)
        {
            return 'n';
        }

        else
        {
            return 'y';
        }
    }
}

// Function to check for repeatition in string
// return 'n' for no repetition else retrun 'y'
char is_rep(string word)
{
    for (int i = 0; i < 26; i++)
    {
        for (int j = i+1; j < 26; j++)
        {
            if (word[i] == word[j])
            {
                return 'y';
            }

            else
            {
                return 'n';
            }
        }
    }
}

