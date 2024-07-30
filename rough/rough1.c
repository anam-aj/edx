#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <strings.h>

unsigned int hash(const char *word);

int main(void)
{
    const char *word = "abc!dasd adwdwd  asd dada adasd adad asd ";
    hash(word);
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int sum = 0;
    int index = 0;
    while (true)
    {
        if (index > strlen(word))
        {
            break;
        }
        else
        {
            sum = sum + (toupper(word[index]) - 'A');
            index++;
        }
    }

    return (sum % 100);
}

