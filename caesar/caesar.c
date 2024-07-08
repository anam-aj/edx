// Program to encrypt msg using caesar cipher

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Funtion declaration
string cipher_text(string text, int key);

int main(int argc, string argv[])
{
    // Checks for no of commnd-line arguments
    if (argc != 2)
    {
        printf("Please give exactly 1 argument\n");
        return 1;
    }

    else
    {
        // Checks if cmnd_line argument contain only digit
        for (int i = 0, len = strlen(argv[1]); i < len; i++)
        {
            if (isdigit(argv[1][i]) == 0)
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }

        // Convert key from string to integer
        int key = atoi(argv[1]);

        // Promt user for input
        string plaintext = get_string("plaintext:  ");

        // Cipher the text and print it
        string ciphertext = cipher_text(plaintext, key);
        printf("ciphertext: %s\n", ciphertext);

        return 0;
    }
}

// Generate ciphertext from plaintext as per key
string cipher_text(string text, int key)
{
    // traverse character of given string one by one
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        // Check if char is uppercase, if yes then cipher it
        if (isupper(text[i]) != 0)
        {
            text[i] = ((text[i] - 'A' + key) % 26) + 'A';
        }

        // Check if char is lowercase, if yes then cipher it
        else if (islower(text[i]) != 0)
        {
            text[i] = ((text[i] - 'a' + key) % 26) + 'a';
        }
    }

    return text;
}
