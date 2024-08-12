# Program to determine reading grade level


def main():

    # Prompts user to enter text
    user_text = input("Please enter the text: ")

    no_of_words = float(word_count(user_text))
    no_of_letters = float(letter_count(user_text))
    no_of_sentences = float(sentence_count(user_text))

    # Calculates Coleman-Liau index
    L = (no_of_letters) / (no_of_words / 100.0)
    S = (no_of_sentences) / (no_of_words / 100.0)
    index = 0.0588 * L - 0.296 * S - 15.8

    # Checks and print grade level
    if index < 0:
        print("Before Grade 1")

    elif index >= 16:
        print("Grade 16+")

    else:
        print("Grade", round(index))


# Function to count words
def word_count(text):

    no_of_spaces = text.count(' ')
    no_of_words = no_of_spaces + 1

    return no_of_words


# Function to count letters
def letter_count(text):

    letters = 0
    for a in text:
        if a.isalpha():
            letters += 1

    return letters


# Funtcion to count sentences
def sentence_count(text):

    no_of_sentences = 0
    for a in text:
        if (a == '.') or (a == '?') or (a == '!'):
            no_of_sentences += 1

    return no_of_sentences


main()
