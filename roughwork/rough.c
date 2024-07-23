#include <stdio.h>

int main(void)
{
    char name[3] = {'a','x', '\0'};
    fopen(name, "w");

    //printf("%p\n", name);

    //FILE *file1 = fopen(name, "w");

}
