# include  <stdio.h>
# define   sqr(x) (x * x)
# define   cub(x) (sqr(x) * x)

int main(void)
{
    int  num;
    printf("Enter a number: ");
    scanf("%d", &num);
    printf(" \n Square of  the number is %d", sqr(num));
    printf(" \n Cube of the number is %d\n", cub(num));
}
