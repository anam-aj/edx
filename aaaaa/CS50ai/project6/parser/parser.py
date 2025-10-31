import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP | VP NP | S Conj S

AP -> Adj | Adj AP
NP -> N | Det NP | AP NP | N PP
PP -> P NP
VP -> V | V NP | V NP PP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """

    # Create tokens
    tokens = nltk.tokenize.word_tokenize(sentence)

    # Convert tokens to lowercase
    tokens = [word.lower() for word in tokens]

    # Remove non-alphabetical words
    for word in tokens:
        alphabetical = False

        for char in word:
            if char.isalpha():
                alphabetical = True
                break

        if not alphabetical:
            tokens.remove(word)

    return tokens


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """

    # Empty list for np_chunks
    NP = []

    # Get all subtrees of the given tree
    subtrees = list(tree.subtrees())

    for t1 in subtrees[1:]:

        # Ensure subtree is NP
        if t1.label() == "NP":
            sub_tr = list(t1.subtrees())
            found = False

            # Ensure validity of NP chunk(i.e. it does not contain any child NP)
            for t2 in sub_tr[1:]:
                if t2.label() == "NP":
                    found = True
                    break

            if not found:
                NP.append(t1)

    return NP


if __name__ == "__main__":
    main()
