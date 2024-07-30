#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(void)

//unsigned int hash(const char *word)
{
    const char *word = "abc";
    int sum = 0;
    int index = 0;
    while (true)
    {
        printf("sum : %i\n", sum);
        printf("index : %i\n", index);

        if (word[index] == '\0')
        {
            break;
        }
        else
        {
            sum = sum + word[index];
            index++;
        }
        printf("sum : %i\n", sum);
        printf("index : %i\n", index);

        printf("\n\n");
    }
}

