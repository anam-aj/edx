#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void change_str(string p);

int main(void)

//unsigned int hash(const char *word)
{
    const char *word = "abc";
    int sum = 0;
    int index = 0;
    while (true)
    {
        if (word[index] == '\0' || index ==  )
        {
            break;
        }
        else
        {
            sum = sum + (toupper(word[index]) - 'A');
            index++;
        }
    }
}

