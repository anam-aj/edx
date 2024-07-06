// Program to determine reading grade level

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string user_text = get_string("Please enter the text: ");
    int no_of_words = word_count(user_text);
    int no_of_letters = letter_count(user_text);
}

// Funtion to count no of spaces between words
int space_count(string text)
{
    int no_of_spaces = 0;
    for (i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == ' ')
        {
            no_of_spaces++;
        }
    }

    return no_of_spaces;
}

// Function to count word in given text
int word_count(string text)
{
    int no_of_words = 0;
    

}
