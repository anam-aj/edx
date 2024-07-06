// Scrabble Game

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Funtions declaration
int score(string word);

int main(void)
{
    // Promt user to enter word
    string p1_word = get_string("Player 1 enter your word: ");
    string p2_word = get_string("Player 2 enter your word: ");

    // Calculate player score
    int p1_score = score(p1_word);
    int p2_score = score(p2_word);

    // Print the winner
    if (p1_score > p2_score)
    {
        printf("Player 1 wins!\n");
    }

    else if (p1_score < p2_score)
    {
        printf("Player 2 wins!\n");
    }

    else
    {
        printf("Tie!\n");
    }
}

// Function to calculate score acoording to scrabble rules
int score(string word)
{

    // Array of letters
    char alphabet[26] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
                        };

    // Array of points
    int points[26] = {1, 3, 3, 2,  1, 4, 2, 4, 1, 8, 5, 1, 3,
                      1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10
                     };

    // Variable for score
    int sum = 0;

    // Traverse given word
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        // extract letter from given word one by one
        // and converts to uppercase(if required)
        char letter = toupper(word[i]);

        // Traverse the alphabet array to match the letter
        for (int j = 0; j < 26; j++)
        {
            // Find the index of matched letter and calculate score
            if (alphabet[j] == letter)
            {
                sum += points[j];
            }
        }
    }

    return sum;
}
