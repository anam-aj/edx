#include <cs50.h>
#include <stdio.h>

int collatz(int number, int counter);

int main(void)
{
    int number = get_int("number: ");

    int steps = collatz(number, 0);

    printf("%i\n", steps);

}

int collatz(int number)
{

    if (number == 1)
    {
        return 0;
    }
    else if (number % 2 == 0)
    {
        return 1 + collatz(number / 2);
    }
    else
    {
        return 1 + collatz((3 * number) + 1);
    }
}
