// Implements a dictionary's functionality

#include "dictionary.h"
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 400;

// Hash table
node *table[N];

// Global variable
int word_count = 0;
bool loaded = false;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    unsigned int hash_value = hash(word);
    node *trav = table[hash_value];
    while (trav != NULL)
    {
        // Check the word
        if (strcasecmp(word, trav->word) == 0)
        {
            return true;
        }

        // Change the pointer to next node
        trav = trav->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int sum = 0;
    int index = 0;
    while (true)
    {
        if (index > strlen(word))
        {
            break;
        }
        else if (isalpha(word[index]))
        {
            sum = sum + (toupper(word[index]) - 'A');
            index++;
        }
        else
        {
            sum = sum + (word[index]);
            index++;
        }
    }

    return (sum % N);
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Intialize pointers in table as NULL
    for (unsigned int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }

    // Open the file to read
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    // Buffer to read word from file
    char *buffer_word = malloc(LENGTH + 1);
    if (buffer_word == NULL)
    {
        return false;
    }

    // Read words from file
    while (fscanf(file, "%s", buffer_word) != EOF)
    {
        // Update word count
        word_count++;

        // Allocate space for node
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }

        // Hash word to node and update linked list pointers
        strcpy(n->word, buffer_word);
        n->next = table[hash(buffer_word)];
        table[hash(buffer_word)] = n;
    }

    // Close file and free buffer
    fclose(file);
    free(buffer_word);

    // Update load success and return true
    loaded = true;
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (loaded)
    {
        return word_count;
    }
    else
    {
        return 0;
    }
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *current = table[i];
        node *ahead = NULL;

        while (current != NULL)
        {
            ahead = current->next;
            free(current);
            current = ahead;
        }
    }

    return true;
}
