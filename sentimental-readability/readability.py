# Program to determine reading grade level


def main()

    # Prompts user to enter text
    user_text = input("Please enter the text: ")

    no_of_words = float(word_count(user_text))
    no_of_letters = float(letter_count(user_text))
    no_of_sentences = float(sentence_count(user_text))

    /// Calculates Coleman-Liau index
    float L = (no_of_letters) / (no_of_words / 100.0);
    float S = (no_of_sentences) / (no_of_words / 100.0);
    float index = 0.0588 * L - 0.296 * S - 15.8;

    // Checks and print grade level
    if (index < 0)
    {
        printf("Before Grade 1\n");
    }

    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }

    else
    {
        printf("Grade %i\n", (int) round(index));
    }
}

// Funtion to count words
int word_count(string text)
{
    int no_of_spaces = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == ' ')
        {
            no_of_spaces++;
        }
    }

    int no_of_words = no_of_spaces + 1;
    return no_of_words;
}

// Function to count letters
int letter_count(string text)
{
    int no_of_letters = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] >= 'a' && text[i] <= 'z')
        {
            no_of_letters++;
        }
        else if (text[i] >= 'A' && text[i] <= 'Z')
        {
            no_of_letters++;
        }
    }

    return no_of_letters;
}

// Funtcion to count sentences
int sentence_count(string text)
{
    int no_of_sentences = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            no_of_sentences++;
        }
    }

    return no_of_sentences;
}
