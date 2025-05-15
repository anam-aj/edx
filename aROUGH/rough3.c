#include <stdio.h>

#define LOOP                                                                                       \
    for (x = 0; x < 5; x++)                                                                        \
    {                                                                                              \
        y = x + 1;                                                                                 \
        printf("%-5.*s\n", y, string);                                                             \
    }                                                                                              \
    for (x = 4; x >= 0; x--)                                                                       \
    {                                                                                              \
        y = x + 1;                                                                                 \
        printf("%-5.*s \n", y, string);                                                            \
    }

int main(void)
{
    int x, y;
    static char string[] = "COBOL";
    printf("\n");
    LOOP;
}
