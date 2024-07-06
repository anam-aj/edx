
#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>



int main(int argc, string argv[])
{
    //int array1[3] = {2,3,4};
    char array2[3] = {'a','b','c'};
    string array3[3] = {"abc","qwe","iop"};

    //int var1 = 2345;
    //char var2 = 'a';
    string var3 = "abc";

    string array4[3] = {"abc", var3, array2};

    //printf("good %i  \n", var1);
    printf("good %s %s %s \n", array4[0], array4[1], array4[2]);
}

