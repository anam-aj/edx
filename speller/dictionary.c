// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 100;

// Hash table
node *table[N];

// Global variable
int word_count = 0;
bool loaded = false;

// Intiale 

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
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
    // TODO: Improve this hash function
    int sum = 0;
    int index = 0;
    while (true)
    {
        if (word[index] == '\0')
        {
            break;
        }
        else
        {
            sum = sum + (toupper(word[index]) - 'A');
            index++;
        }
    }

    return (sum % 100);
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open the file to read
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    // Read word from file
    char *buffer_word = malloc(sizeof(LENGTH + 1));
    if (buffer_word == NULL)
    {
        return false;
    }
    while (fscanf(file, "%s", buffer_word) != EOF)
    {
        word_count++;
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        strcpy(n->word, buffer_word);
        //n->next = NULL;

        // Hash word to node
        n->next = table[hash(buffer_word)];
        table[hash(buffer_word)] = n;
    }

    // Close file and free buffer
    free(buffer_word);
    fclose(file);
    loaded = true;
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
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
    // TODO
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
    return false;
}
