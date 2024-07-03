// Print the the no of minimum coins
#include <cs50.h>
#include <stdio.h>

int check_sum(long number);

int main(void)
{
    long number;
    // Promts the user to enter card no
    do
    {
        number = get_long("Enter Card Number: ");
    }
    while (number <= 0);


    int sum_of_even_place_digits = 0;
    int sum_of_odd_place_digits = 0;
    int i = 1;

    while (number > 0)
    {
        printf("--%i\n", i);
        int digit_at_odd_place = number % 10;
        printf("odd %i\n", digit_at_odd_place);
        sum_of_odd_place_digits += digit_at_odd_place;
        number = (number / 10);
        printf("%li\n", number);

        int digit_at_even_place = number % 10;
        printf("even %i\n", digit_at_even_place);
        sum_of_even_place_digits += digit_at_even_place;
        number = (number / 10);
        printf("%li\n", number);
        i++;
    }

    int net_sum = (sum_of_odd_place_digits) + (2 * sum_of_even_place_digits);
    printf("%i\n", net_sum);
    int unit_digit = net_sum % 10;
    printf("%i\n", unit_digit);
}
