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
    if ((argc == 2) && (isstrdigit(argv[1]) == 0))
    {
        str

        // Promts user for plaintext
        string plain_text = get_string("plaintext:  ");

        // Generate ciphertext using function and prints it
        string cipher_text = ciphertext(plain_text);
        printf("ciphertext: %s\n", cipher_text);

        return 1;
    }

    else
    {
        printf("Program requires integer key! Usage format: ./caesar key");
        return 0;
    }
}

// convert plaintext into ciphertext
string ciphertext(string plaintext)
{
    // Traverse one by one each character of given text
    for (int i = 0, len = strlen(plaintext); i < len; i++)
    {
        // check if character is uppercase letter
        if (isupper(plaintext[i]) != 0)
        {
            // Cipher the letter
            int p_i = plaintext[i] - 'A';
            int c_i = (p_i + atoi(argv[1])) % 26;
            plaintext[i] = c_i + 'A';
        }

        // check if character is lower case letter
        else if (islower(plaintext[i]) != 0)
        {
            // Cipher the letter
            int p_i = plaintext[i] - 'a';
            string a = argv[1];
            int c_i = p_i + atoi(a) % 26;
            plaintext[i] = c_i + 'a';
        }
    }

    return plaintext;
}

// Checks if string contains only digits(0-9)
int isstrdigit(string str)
{
    for (int i = 0, len = strlen(str); i < len; i++)
    {
        if (str[i] >= 48 && str[i] <=57)
        {
        }
        else
        {
            return 1;
        }
    }

    return 0;
}
