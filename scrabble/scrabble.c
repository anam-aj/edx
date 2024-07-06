// Scrabble Game

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Promt user to enter word
    string p1_word = get_string("Player 1 enter your word");
    string p2_word = get_string("Player 2 enter your word");

}

// Function to calculate score acoording to scrabble rules
int score(string word)
{

    // Array of letters
    char alphabet[26] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}

    // Array of characters
    int points[26] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3
                      1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    int sum = 0;

    for (int i = 0, n = strlen(word); i < n; i++)
    {
        // Converts character to uppercase
        char letter = toupper(word[i]);

        for (int j = 0; j < 26; j++)
        {
            if 
        }
    }


}
