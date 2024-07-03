// Print the the no of minimum coins
#include <cs50.h>
#include <stdio.h>

int check_sum(long number);




int check_sum(long number)
{
    int sum_of_even_place_digits = 0;
    int sum_of_odd_place_digits = 0;

    while (number > 0)
    {
        int digit_at_odd_place = number % 10;
        sum_of_odd_place_digits += digit_at_odd_place;
        number = (number / 10);

        int digit_at_even_place = number % 10;
        sum_of_even_place_digits += digit_at_even_place;
        number = (number / 10);
    }

    int net_sum = (sum_of_odd_place_digits) + (2 * sum_of_even_place_digits);
    int unit_digit = net_sum % 10;
    return unit_digit;
}
