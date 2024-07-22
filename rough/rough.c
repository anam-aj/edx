#include <stdio.h>

int main(void)
{
    FILE *file = fopen("cs5033.txt", "w");
    //if (file != NULL)
    //{
        //fprintf(file, "This is CS50\n");
        fclose(file);
    //}
}
