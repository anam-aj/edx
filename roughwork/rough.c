#include <stdio.h>

int main(void)
{
    char *s;
    //printf("%p\n", s);

    s = "asdf";
    printf("%p\n", s);
    printf("%p\n", &s);


    printf("%s\n", s);


    s = "xyz";
    printf("%p\n", s);
    printf("%p\n", &s);


    printf("%s\n", s);

    //char *name[4];
    //name[0] = ;
    //name[1] = ;
    //name[2] = ;
    //name[3] = ;

    //printf("%p\n", name);

    //FILE *file1 = fopen(name, "w");

}
