

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>



int main(int argc, string argv[])
{
    int array1[3] = {2,3,4};
    char array2[3] = {'a','b','c'};
    string array3[3] = {"abc","qwe","iop"};

    int var1 = 4567;
    char var2 = 't';
    string var3 = "ghj";

    char array4[3] = {2, var2, var1};

    //printf("good %i  \n", var2);
    printf("good %i %i %i \n", array4[0], array4[1], array4[2]);
}

