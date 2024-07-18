#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

void swap(int *a, int *b);

int main(void)
{
    int x = 10;
    int y = 112;

    int* a = &x;
    int* b = &y;
    swap(a, b);
    printf("x is %i  y is %i\n", x, y);
}

void swap(int *q, int *r)
{
    int temp = *q;
    *q = *r;
    *r = temp;
}
