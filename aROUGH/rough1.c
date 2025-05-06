/* Program tests a string for a palindrome using pointer notation */
# include <stdio.h>
# include <conio.h>
# include <stdlib.h>

short int palindrome(char,int); /*Function Prototype */

int main(void)
{
    char *palin, c;
    int i, count;

    palin =(char *) malloc(20 * sizeof(char));
    printf("\nEnter a word: ");

    do {
    c = getchar();
    palin[i] = c;
    i++;
    }while(c != '\n');

    i = i-1;
    palin[i] = '\0';
    count = i;
    if(palindrome(palin,count) == 1)
        printf("\nEntered word is not a palindrome.");
    else
        printf("\nEntered word is a palindrome");
}


short int palindrome(char *palin, int len)
{
    short int i = 0, j = 0;
    for(i=0 , j=len-1; i < len/2;i++,j--)
    {
        if(palin[i] == palin[j])
            continue;
        else
            return(1);
    }
    return(0);
}
