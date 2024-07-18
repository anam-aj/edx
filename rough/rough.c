#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

//void swap(int *a, int *b);

int main(void)
{
    int x = 10;
    //int y = 112;

    int *a = &x;
    //int *b = &y;
    //swap(a, b);
    printf("x is %p \n", &x);
    printf("x is %p \n", a);
    printf("x is %i \n", *&x);
    printf("x is %i \n", *a);
}

//void swap(int *q, int *r)
//{
    //int temp = *q;
    //*q = *r;
    //*r = temp;
//}
