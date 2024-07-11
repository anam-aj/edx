#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // int array1[2][3] = {{1, 2 ,3}, {4 ,5 ,6}};

    int a[2] = {1, 2};
    int b[2] = {3, 4};
    int c[2] = {5, 6};



    int d[3][2] = {{1, 2}, {3, 4}};
    int e = d[2][1];

    printf("%i\n",e);
}
