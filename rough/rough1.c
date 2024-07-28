#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node
{
    string phrase;
    int number;
} node;

int main(void)
{
    node one;
    one.phrase = "xyz";
    one.number = 123;

    printf("%s %i\n", one.phrase, one.number);
}

