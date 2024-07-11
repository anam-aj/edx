#include <cs50.h>
#include <stdio.h>

int collatz(int number);

int main(void)
{
    int number = get_int("number: ");

    int steps = collatz(number, 0);

    printf("%i\n", steps);

}

int collatz(int number, int counter)
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
        return collatz((3 * number + 1) / 2)
    }
}
