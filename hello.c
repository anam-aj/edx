#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name = get_string("Please enter you name: ");
    int age = get_int("Please enter your age: ");
    int number = get_int("Please enter your contact number: ");

    printf("Name: %s\n Age: %i\n Caontact number: %i%n", name, age, number);
}
