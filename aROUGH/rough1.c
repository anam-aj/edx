#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <strings.h>
#include <string.h>

unsigned int hash(const char *word);

int main(void)
{
    char name[80];
    int length;
    printf("Enter your name: ");
    gets(name);
    length=strlen(name);
    printf("Your name has %d characters\n", length); }
}

/*// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int sum = 0;
    int index = 0;
    while (true)
    {
        printf("sum %i ", sum);
        printf("ind %i ", index);
        printf("chr %c\n", word[index]);
        if (index > strlen(word))
        {
            break;
        }
        else
        {
            sum = sum + (toupper(word[index]) - 'A');
            index++;
        }
        printf("sum %i ", sum);
        printf("ind %i ", index);
        printf("chr %c\n", word[index]);

        printf("\n\n");
    }


    return (sum % 100);
}
*/
