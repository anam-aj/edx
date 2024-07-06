// Program to determine reading grade level

#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Funtion declaration(in the order they are defined)
int space_count(string text);
int word_count(string text);
int letter_count(string text);
int sentence_count(string text);

int main(void)
{
    // Prompts user to enter text
    string user_text = get_string("Please enter the text: ");

    int no_of_words = word_count(user_text);
    int no_of_letters = letter_count(user_text);
    int no_of_sentences = sentence_count(user_text);


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

// Function to count words
int word_count(string text)
{
    int spaces = space_count(text);
    int words = spaces + 1;

    return words;
}

// Function to count letters
int letter_count(string text)
{
    int spaces = space_count(text);
    int no_of_letters = strlen(text) - spaces;

    return no_of_letters;
}

// Funtcion to count sentences
int sentence_count(string text)
{
    int no_of_sentences = 0;
    for (i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == '.')
        {
            no_of_sentences++;
        }
    }

    return no_of_sentences;
}
