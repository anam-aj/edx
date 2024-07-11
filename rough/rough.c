#include <cs50.h>
#include <stdio.h>

int collatz(int number);

int main(void)
{
    int counter = 0;

    printf("%s\n", winner);

}

int collatz(int number)
{

    if (number == 1)
    {
        return counter;
    }
    else if (number % 2 == 0)
    {
        counter++;
        return collatz(number / 2);
    }
    else
    {
        counter++;
        return collatz(3 * number + 1 / 2)
    }
}
