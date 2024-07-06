
#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>



int main(int argc, string argv[])
{
    //int array1[3] = {'a',3,4};
    char array2[3] = {'a','b','c'};
    string array3[3] = {"abc","qwe","iop"};

    //int var1 = 2345;
    //char var2 = 'a';
    string var3 = "abc";

    string array4[3] = {"abc", array2, var3};

    //printf("good %i  \n", array1[0]);
    printf("good %s %s %s \n", array4[0], array4[1], array4[2]);
}

