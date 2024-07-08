// Program to encrypt text using substitution key

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function declaration(in order they are defined)
string cipher_text(string text, string key);
char is_str_alpha(string word);
char is_rep(string word);

int main(int argc, string argv[])
{
    // Check for no of arguments(1) and its length(26)
    // if not prints error msg
    if ((argc != 2) || (strlen(argv[1]) != 26))
    {
        printf("Give only 1 argument, 26 alphabets, no repetition\n");

        return 1;
    }

    // Checks if argument alphabetical and for repetition
    // prints error msg accordingly
    if ((is_str_alpha(argv[1]) == 'n') || (is_rep(argv[1]) == 'y'))
    {
        printf("Give only 1 argument, 26 alphabets, no repetition\n");

        return 1;
    }

    string key = argv[1];

    // Promt user for plaintext
    string plaintext = get_string("plaintext:  ");

    // Convert plaintext to ciphertext and print it
    string ciphertext = cipher_text(plaintext, key);
    printf("ciphertext: %s\n", ciphertext);

    return 0;
}

// Funtion to convert plaintext to ciphertext
// by substitution from 'key'
string cipher_text(string text, string key)
{
    // traverse character of given string one by one
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        // Check if char is uppercase letter, if yes then cipher it
        if (isupper(text[i]) != 0)
        {
            int j = text[i] - 'A';
            text[i] = toupper(key[j]);
        }

        // Check if char is lowercase letter, if yes then cipher it
        else if (islower(text[i]) != 0)
        {
            int j = text[i] - 'a';
            text[i] = tolower(key[j]);
        }
    }

    return text;
}

// Function to check if string is alphabetical
// return 'y' if string has only alphabet else return 'n'
char is_str_alpha(string word)
{
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        if (isalpha(word[i]) == 0)
        {
            return 'n';
        }
    }

    return 'y';
}

// Function to check for repeatition in string
// return 'n' for no repetition else retrun 'y'
char is_rep(string word)
{
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        for (int j = i + 1; j < len; j++)
        {
            if (word[i] == word[j])
            {
                return 'y';
            }
        }
    }

    return 'n';
}
